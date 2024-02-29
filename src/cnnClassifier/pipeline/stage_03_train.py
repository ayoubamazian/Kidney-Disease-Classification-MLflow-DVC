import sys
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_train import Training
from cnnClassifier.exception import CustomException


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        