from src.MLFlowProject import logger
from src.MLFlowProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.MLFlowProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.MLFlowProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.MLFlowProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

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

    logger.info(">>>>>> stage 03 data transformation started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(">>>>>> stage 03 data transformation completed <<<<<<\n\nx==========x")

    logger.info(">>>>>> stage 04 model trainer started <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(">>>>>> stage 04 model trainer completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 
