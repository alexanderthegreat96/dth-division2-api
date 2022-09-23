import mysql.connector
from mysql.connector import errors
import time
from classes.ApiConfig import ApiConfig


class DatabaseWrapper:
    def __init__(self):
        config = ApiConfig()
        self.connection = mysql.connector.connect(
            host=config.mysqlHost(),
            database=config.mysqlDb(),
            user=config.mysqlUser(),
            password=config.mysqlPass(),
        )
        self.cursor = self.connection.cursor()
        self.now = time.strftime('%Y-%m-%d %H:%M:%S')

    def __del__(self):
        self.cursor.close()
        self.connection.close()
