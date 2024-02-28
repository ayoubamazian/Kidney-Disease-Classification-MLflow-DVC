import sys
from src.cnnClassifier.exception import CustomException
from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import  DataIngestionPipeline


STAGE_NAME_1 = 'data ingestion Stage'
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME_1} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME_1} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)