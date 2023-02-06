import logging

def setup_logger(logger_name: str, log_file: str, level: int = logging.INFO):
    """
    Setup logger with the specified filename
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    return logger

logger = setup_logger('etl_car_sales_process', 'etl_process.log')
