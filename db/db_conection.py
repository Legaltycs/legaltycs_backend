import pymysql
from os import getenv


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
                port=int(getenv('PORT')),
                host=getenv('HOST'),
                user=getenv('USER'),
                password=getenv('PASS'),
                db=getenv('DB')
        )
        self.cursor = self.connection.cursor()
