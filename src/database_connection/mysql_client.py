import mysql.connector

class MySQLClient:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def insert(self, table, columns, values_list):
        placeholders = ', '.join(['%s'] * len(columns))
        columns = ', '.join(columns)
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cursor.executemany(sql, values_list)

