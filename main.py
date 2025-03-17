from src.MLFlowProject import logger
from src.MLFlowProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.MLFlowProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

logger.info("Welcome to MLFlow Project")

try:
    logger.info(">>>>>> stage 01 data ingestion started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>>>> stage 01 data ingestion completed <<<<<<\n\nx==========x")

    logger.info(">>>>>> stage 02 data validation started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(">>>>>> stage 02 data validation completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 
