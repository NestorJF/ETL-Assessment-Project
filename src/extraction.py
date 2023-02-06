import pandas as pd

class Extraction:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def extract_data(self, datasource: str = "csv"):
        dataset = pd.DataFrame()
        if datasource == "csv":
            dataset = self._extract_from_csv()
        else:
            print("No datasource")
        return dataset
        
    def _extract_from_csv(self):
        """
        Reads the CSV file specified in the constructor and returns a Pandas DataFrame
        :return: DataFrame containing the extracted data            
        """
        data = pd.read_csv(self.file_path, thousands=',')
        return data