import sys
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation_withmlflow import Evaluation
from cnnClassifier.exception import CustomException

class ModelEvaluationPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()