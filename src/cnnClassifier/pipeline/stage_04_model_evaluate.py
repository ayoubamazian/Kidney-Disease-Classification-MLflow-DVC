import sys
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation_withmlflow import Evaluation
from cnnClassifier.exception import CustomException
from cnnClassifier import logger

class ModelEvaluationPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()
        # evaluation.log_into_mlflow()

STAGE_NAME = "model evaluation stage"

if __name__ == '__main__':

    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e, sys)