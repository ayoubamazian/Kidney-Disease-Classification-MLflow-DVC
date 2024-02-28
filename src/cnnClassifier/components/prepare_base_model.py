import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    @staticmethod
    def save_model(model: tf.keras.Model, path:Path):
        model.save(path)
    
    def download_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            include_top=self.config.params_include_top,
            weights=self.config.params_weights,
            input_shape=self.config.params_image_size
        )
        
        self.save_model(model=self.model, path=self.config.base_model_path)

    @staticmethod    
    def _prepare_full_model(model, classes, freez_all, freez_till, lr):
        if freez_all:
            for layer in model.layers:
                layer.trainable = False

        if freez_till is not None and freez_till > 1:
            for layer in model.layers[:freez_till]:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        dense_out = tf.keras.layers.Dense(classes, activation='softmax')(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=dense_out
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=['accuracy']
        )

        full_model.summary()

        return full_model
    
    def updated_model(self):
        self.full_model = self._prepare_full_model(
            model = self.model,
            classes = self.config.params_classes,
            freez_all = False,
            freez_till = None,
            lr = self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    