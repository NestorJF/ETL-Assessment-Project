import mysql.connector

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
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Commit any pending transactions, close the cursor, and close the connection.
        """
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def insert(self, table: str, columns_list: list[str], values_list: list):
        """
        Insert multiple rows into a table in the MySQL database.
        """
        placeholders = ', '.join(['%s'] * len(columns_list))
        columns = ', '.join(columns_list)
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cursor.executemany(sql, values_list)

