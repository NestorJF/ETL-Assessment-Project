import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
    TABLE_COLUMNS = ['date', 'car', 'car_model', 'value', 'sales_person', 'city', 'country', 'year_of_the_sale']
    TABLE_NAME = "car_sale"
    DATASET_DEFAULT_PATH = "data/input/car_sales_dataset.csv"


CONFIG = Config()
