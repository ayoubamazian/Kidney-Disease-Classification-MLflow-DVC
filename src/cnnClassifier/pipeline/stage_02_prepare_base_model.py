from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.exception import CustomException
import sys
from cnnClassifier.logging import logging

STAGE_NAME = "Prepare base model"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.download_base_model()
            prepare_base_model.updated_model()
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == '__main__':

    try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e, sys)