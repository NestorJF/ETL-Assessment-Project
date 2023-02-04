from src.extract import Extract


if __name__ == "__main__":
    extract = Extract("data/input/car_sales_dataset.csv")
    dataset = extract.extract_data("csv")
    print("Hi")
    print(dataset)