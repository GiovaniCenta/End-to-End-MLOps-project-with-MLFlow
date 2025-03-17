import os
import pandas as pd
from src.MLFlowProject import logger
from src.MLFlowProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True

            if not os.path.exists(self.config.unzip_data_dir):
                validation_status = False
                with open(self.config.STATUS_FILE, 'a') as f:
                    f.write(f"Validation status: {validation_status}, File is missing: {self.config.unzip_data_dir}\n")
            else:
                with open(self.config.STATUS_FILE, 'a') as f:
                    f.write(f"Validation status: {validation_status}, File exists: {self.config.unzip_data_dir}\n")

            return validation_status

        except Exception as e:
            raise e

    def validate_schema(self) -> bool:
        try:
            validation_status = True
            data = pd.read_csv(self.config.unzip_data_dir)

            # Check if all required columns exist
            for column in self.config.all_schema['COLUMNS']:
                if column not in data.columns:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"Validation status: {validation_status}, Column is missing: {column}\n")
                else:
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"Validation status: {validation_status}, Column exists: {column}\n")

            # Check if target column exists
            if self.config.all_schema['TARGET_COLUMN'] not in data.columns:
                validation_status = False
                with open(self.config.STATUS_FILE, 'a') as f:
                    f.write(f"Validation status: {validation_status}, Target column is missing: {self.config.all_schema['TARGET_COLUMN']}\n")
            else:
                with open(self.config.STATUS_FILE, 'a') as f:
                    f.write(f"Validation status: {validation_status}, Target column exists: {self.config.all_schema['TARGET_COLUMN']}\n")

            return validation_status

        except Exception as e:
            raise e 