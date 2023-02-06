import mysql.connector
from logger import logger


class MySQLClient:
    """
    A class that represents a client for connecting to a MySQL database.
    """
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def __enter__(self):
        """
        Connect to the MySQL database and return the MySQLClient instance.
        """
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            logger.info("Connected to MySQL Database")
            return self
        except mysql.connector.Error as e:
            logger.exception("Error while connecting to MySQL:", exc_info=e)           

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Commit any pending transactions, close the cursor and close the connection.
        """
        self.conn.commit()
        self._close_connection()

    def insert(self, table_name: str, columns_list: list[str], values_list: list):
        """
        Insert multiple rows into a table in the MySQL database.
        """
        placeholders = ', '.join(['%s'] * len(columns_list))
        columns = ', '.join(columns_list)
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        try:
            self.cursor.executemany(sql, values_list)
            self.conn.commit()
            logger.info(f"{self.cursor.rowcount} record(s) inserted successfully into {table_name} table")
        except mysql.connector.Error as e:
            logger.exception("Failed to insert record into {table_name} table", exc_info=e)
    
    def _close_connection(self):
        """
        Close the cursor and close the connection to the MySQL Database.
        """
        try:
            self.cursor.close()
            self.conn.close()
        except mysql.connector.Error as e:
            logger.exception("Error while closing MySQL connection:", exc_info=e)
        else:
            logger.info("Closed connection to MySQL Database")


