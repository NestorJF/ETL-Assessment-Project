import pandas as pd


class Transformation:
    def __init__(self, datasource, dataset):
        self.datasource = datasource
        self.dataset = dataset

    def start_transformation(self):
        if self.datasource == "csv":
            new_dataset = self._transform_dataframe()
        else:
            print("Datasource not found. Transformation failed.")
            new_dataset = self.dataset
        return new_dataset

    def _transform_dataframe(self):
        new_dataset = self.dataset.copy()
        new_dataset = new_dataset.dropna()
        new_dataset["Date"] = pd.to_datetime(new_dataset["Date"])
        new_dataset["Year of the Sale"] = new_dataset["Date"].dt.strftime('%Y')
        new_dataset["Date"] = new_dataset["Date"].dt.strftime('%m/%d/%Y')
        new_dataset['Car Model'] = new_dataset['Car Model'].astype('category')
        new_dataset['Car Model'] = new_dataset['Car Model'].cat.codes
        return new_dataset