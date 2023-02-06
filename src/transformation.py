import pandas as pd


class Transformation:
    def __init__(self, datasource, dataset):
        self.datasource = datasource
        self.dataset = dataset

    def start_transformation(self):
        if self.datasource == "csv":
            new_dataframe = self._transform_dataframe()
            print(new_dataframe)
            transformed_dataset = self._convert_dataframe_to_list(new_dataframe)
            print("transformed")
            print(transformed_dataset)
            return transformed_dataset
        else:
            print("Datasource not found. Transformation failed.")
        
    def _transform_dataframe(self):
        new_dataset = self.dataset.copy()
        new_dataset = new_dataset.dropna()
        new_dataset["Date"] = pd.to_datetime(new_dataset["Date"])
        new_dataset["Year of the Sale"] = new_dataset["Date"].dt.strftime('%Y')
        new_dataset["Date"] = new_dataset["Date"].dt.strftime('%Y-%m-%d')
        new_dataset['Car Model'] = new_dataset['Car Model'].astype('category')
        new_dataset['Car Model'] = new_dataset['Car Model'].cat.codes
        new_dataset['Value in USD'] = new_dataset['Value in USD'].astype(float)
        return new_dataset

    def _convert_dataframe_to_list(self, dataframe):
        return dataframe.values.tolist()