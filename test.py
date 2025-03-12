from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger = get_logger(__name__)

def divide_number(a,b):
    try:
        result= a/b
        logger.info(f"divide number {a} and {b} is {result}")
        return result
    except Exception as e:
        logger.error("Error occurred while dividing number",exc_info=True)
        raise CustomException("custom error zero",sys)
    
if __name__ == "__main__":
    try:
        logger.info("Starting the application")
        divide_number(10,0)
    except CustomException as ce:
        logger.error(str(ce))