import os
import sys
from dataclasses import dataclass

from src.MLFlowProject.config.configuration import ConfigurationManager
from src.MLFlowProject.components.model_trainer import ModelTrainer
from src.MLFlowProject import logger

@dataclass
class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e