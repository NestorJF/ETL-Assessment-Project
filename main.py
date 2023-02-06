from src.extraction import Extraction
from src.transformation import Transformation
from src.data_loader import DataLoader
from config import CONFIG






if __name__ == "__main__":
    extract = Extraction(CONFIG.DATASET_DEFAULT_PATH)
    dataset = extract.extract_data("csv")
    transform = Transformation(dataset)
    new_dataset = transform.start_transformation()
    data_loader = DataLoader(new_dataset)
    data_loader.insert_into_mysql_db(CONFIG.TABLE_NAME, CONFIG.TABLE_COLUMNS)
