from db.db_conection import DataBase
from models.userModel import User


class UserRepository:
    def __init__(self):
        self.database = DataBase()
        self.cursor = self.database.cursor

    def find_user(self, name, password):
        sql = 'SELECT COUNT(*) FROM user WHERE name = \'{0}\' AND password = \'{1}\';'.format(name, password)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            return user[0]

        except Exception as e:
            print(e)

    def create_user(self, data: User):
        print(data)
