import sys
from cnnClassifier.exception import CustomException
from cnnClassifier.logging import logging
from cnnClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline


STAGE_NAME_1 = 'Data Ingestion Stage'
try:
    logging.info(f"Stage {STAGE_NAME_1} started")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f"Stage {STAGE_NAME_1} completed")
except Exception as e:
    raise CustomException(e, sys)