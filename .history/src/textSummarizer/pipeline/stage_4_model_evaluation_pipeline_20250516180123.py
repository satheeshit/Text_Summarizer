from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_evaluation import ModelEvaluation
from src.textSummarizer.logging import logger


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    def initiative_model_evaluation(self):
        config= ConfigurationManager()
        model_trainer_config=config.get_model_evaluation_config()
        model_trainer_config=ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
