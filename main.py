import sys
from cnnClassifier.exception import CustomException
from cnnClassifier.logging import logging
from cnnClassifier.pipeline.stage_03_train import  ModelTrainingPipeline


STAGE_NAME_1 = 'train model Stage'
try:
    logging.info(f"*******************")
    logging.info(f">>>>>> stage {STAGE_NAME_1} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME_1} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)