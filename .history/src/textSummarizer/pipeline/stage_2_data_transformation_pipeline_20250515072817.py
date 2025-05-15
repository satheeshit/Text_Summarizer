from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_ingestion import Data
from src.textSummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiative_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.convert()