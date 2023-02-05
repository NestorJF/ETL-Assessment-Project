from src.extract import Extract
from src.transform import Transformation


if __name__ == "__main__":
    extract = Extract("data/input/car_sales_dataset.csv")
    dataset = extract.extract_data("csv")
    transform = Transformation("csv", dataset)
    new_dataset = transform.start_transformation()
    print(dataset)
    print("New dataset", new_dataset.head(190).to_string())