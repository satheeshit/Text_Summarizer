from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_trainer import ModelTrainer
from src.textSummarizer.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def initiative_model_trainer(self):
        config= ConfigurationManager()
        model_trainer_config=config.model_trainer_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.convert()