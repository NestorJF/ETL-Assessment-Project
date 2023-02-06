import pandas as pd

class Extraction:
    """
    This class is used to extract data from a dataset. Currently, it only supports CSV file.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        
    def extract_data(self, datasource: str = "csv"):
        """
        Extracts the data based on the datasource specified
        :return: the extracted dataset
        """
        if datasource.lower() == "csv":
            dataset = self._extract_from_csv()
            return dataset
        else:
            print("No data source found.")
        
    def _extract_from_csv(self):
        """
        Reads the CSV file specified in the constructor and returns a Pandas DataFrame
        :return: DataFrame containing the extracted data            
        """
        data = pd.read_csv(self.file_path, thousands=',')
        return data