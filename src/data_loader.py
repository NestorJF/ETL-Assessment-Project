from src.db_connector.mysql_client import MySQLClient


class DataLoader:
    """
    The DataLoader class is used to load data into a MySQL database. 
    """
    def __init__(self, data_values):
        self.data_values = data_values

    def insert_into_mysql_db(self, table, table_columns):
        """
        Open connection and inserts the data values into a MySQL database table.
        """
        with MySQLClient(host='', user='', password='', database='') as client:
            client.insert(table, table_columns, self.data_values)
    
    

