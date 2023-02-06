from extraction import Extraction
from transformation import Transformation
from data_loader import DataLoader

if __name__ == "__main__":
    extract = Extraction("data/input/car_sales_dataset.csv")
    dataset = extract.extract_data("csv")
    transform = Transformation("csv", dataset)
    new_dataset = transform.start_transformation()
    print(new_dataset)
    columns = ['date', 'car', 'car_model', 'value', 'sales_person', 'city', 'country', 'year_of_the_sale']
    table = "car_sale"
    data_loader = DataLoader(new_dataset)
    data_loader.insert_into_mysql_db(table, columns)
