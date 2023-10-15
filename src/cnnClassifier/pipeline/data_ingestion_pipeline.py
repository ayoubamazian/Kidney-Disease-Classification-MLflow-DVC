from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.exception import CustomException
import sys

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            # data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise CustomException(e, sys)