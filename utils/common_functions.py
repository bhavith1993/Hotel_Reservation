import os
import pandas as pd
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"yaml file: {file_path} not found")
        with open(file_path, "rb") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return config
    except Exception as e:
        logger.error("Error reading yaml file",exc_info=True)
        raise CustomException("Failed to read YAML file", e)
    
    
def load_data(path):
    try:
        logger.info(f"Loading data from {path}")
        return pd.read_csv(path)
    except Exception as e:
        logger.error("Error while loading data {e}")
        raise CustomException("Failed to load data", e)
    
