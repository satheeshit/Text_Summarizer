from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def initiative_data_ingestion(self):
        config=ConfigurationManager()
        
data_ingestion_config=config.get        