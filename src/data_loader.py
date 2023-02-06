from src.db_connector.mysql_client import MySQLClient


class DataLoader:
    def __init__(self, data_values):
        self.data_values = data_values

    def insert_into_mysql_db(self, table, table_columns):
        with MySQLClient(host='', user='', password='', database='') as client:
            client.insert(table, table_columns, self.data_values)
    
    

