import pandas as pd

class Extract:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def extract_from_csv(self):
        """
        Reads the CSV file specified in the constructor and returns a Pandas DataFrame
        :return: DataFrame containing the extracted data            
        """
        data = pd.read_csv(self.file_path)
        return data