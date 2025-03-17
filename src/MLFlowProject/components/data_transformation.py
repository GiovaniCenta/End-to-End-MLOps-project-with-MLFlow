import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.MLFlowProject import logger
from src.MLFlowProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        try:
            # Read the data
            data = pd.read_csv(self.config.data_path)
            
            # Split the data
            train, test = train_test_split(data)

            # Save the train and test data
            train_data_path = os.path.join(self.config.root_dir, "train.csv")
            test_data_path = os.path.join(self.config.root_dir, "test.csv")

            train.to_csv(train_data_path, index=False)
            test.to_csv(test_data_path, index=False)

            logger.info(f"Splited data into training and test sets")
            logger.info(f"Training data shape: {train.shape}")
            logger.info(f"Test data shape: {test.shape}")

            return train_data_path, test_data_path

        except Exception as e:
            raise e 