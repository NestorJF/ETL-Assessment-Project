import pandas as pd


class Transformation:
    """
    This class is responsible for transforming a dataset into a desired format.
    """
    def __init__(self, datasource, dataset):
        self.datasource = datasource
        self.dataset = dataset

    def start_transformation(self):
        """
        The main method of the class, it starts the transformation process based on the type of the dataset.
        :return: A list with the transformed dataset.
        """
        transformed_dataset = None
        if isinstance(self.datasource, pd.DataFrame):
            new_dataframe = self._transform_dataframe()
            transformed_dataset = self._convert_dataframe_to_list(new_dataframe)
        else:
            print("TO DO: Add a new transformation process for this type of dataset.")
        return transformed_dataset
        
    def _transform_dataframe(self):
        """
        Transforms a pandas dataframe into a desired format:
        - Remove any rows with missing values.
        - Convert the date columns to a standard format.
        - Create a new column to store the year of the sale.
        - Replace the categorical values in the "Car Model" column with numerical values.
        - Convert Value in USD Column to float type.
        :return: The transformed dataframe.
        """
        new_dataset = self.dataset.copy()
        new_dataset = new_dataset.dropna()
        new_dataset["Date"] = pd.to_datetime(new_dataset["Date"])
        new_dataset["Year of the Sale"] = new_dataset["Date"].dt.strftime('%Y')
        new_dataset["Date"] = new_dataset["Date"].dt.strftime('%Y-%m-%d')
        new_dataset['Car Model'] = new_dataset['Car Model'].astype('category')
        new_dataset['Car Model'] = new_dataset['Car Model'].cat.codes
        new_dataset['Value in USD'] = new_dataset['Value in USD'].astype(float)
        return new_dataset

    def _convert_dataframe_to_list(self, dataframe: pd.DataFrame):
        """
        Converts a pandas dataframe into a list.
        """
        return dataframe.values.tolist()