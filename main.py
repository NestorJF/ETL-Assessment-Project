from src.extraction import Extraction
from src.transformation import Transformation
from src.data_loader import DataLoader
from config import CONFIG
from logger import logger




if __name__ == "__main__":
    logger.info("################# Starting ETL Process for Car Sales Dataset #################")
    try:
        logger.info("------- Starting to Extract information from dataset --------")
        extract = Extraction(CONFIG.DATASET_DEFAULT_PATH)
        dataset = extract.extract_data("csv")
        logger.info("-------Extract information from dataset finished -------")
        logger.info("------- Starting to transform the dataset -------")
        transform = Transformation(dataset)
        new_dataset = transform.start_transformation()
        logger.info("------- Transformation of dataset finished -------")
        if new_dataset:
            logger.info("------- Starting to load the transformed data to MySQL -------")
            data_loader = DataLoader(new_dataset)
            data_loader.insert_into_mysql_db(CONFIG.TABLE_NAME, CONFIG.TABLE_COLUMNS)
            logger.info("------- Load the transformed data to MySQL finished -------")
    except Exception as e:
        logger.exception("ETL Process failed: ", exc_info=e)
    logger.info("#################The ETL Process for Car Sales Dataset has finished #################")
