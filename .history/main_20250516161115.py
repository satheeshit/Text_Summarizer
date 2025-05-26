from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerTrainingPipeline


STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiative_data_ingestion()
    logger.info(f"stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e    
        

STAGE_NAME="Data Transformation stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataTransformationTrainingPipeline()
    data_ingestion_pipeline.initiative_data_transformation()
    logger.info(f"stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e  

STAGE_NAME="Model Trainer stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline=ModelTrainerTrainingPipeline()
   model_trainer_pipeline.initiative_data_transformation()
    logger.info(f"stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e  