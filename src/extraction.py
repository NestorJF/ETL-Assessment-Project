import pandas as pd
from logger import logger

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
            logger.error("Datasource not valid. Please check.")
            return None
        
    def _extract_from_csv(self):
        """
        Reads the CSV file specified in the constructor and returns a Pandas DataFrame
        :return: DataFrame containing the extracted data            
        """
        try:
            data = pd.read_csv(self.file_path, thousands=',')
        except FileNotFoundError as e:
            logger.exception("File not found: ", exc_info=e)
        except UnicodeDecodeError as e:
            logger.exception("This file is not a valid CSV format. Please check:", exc_info=e)
        else:
            return data