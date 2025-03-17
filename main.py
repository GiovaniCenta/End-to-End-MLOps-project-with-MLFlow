from src.MLFlowProject import logger
from src.MLFlowProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

logger.info("Welcome to MLFlow Project")

try:
    logger.info(">>>>>> stage 01 data ingestion started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>>>> stage 01 data ingestion completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 
