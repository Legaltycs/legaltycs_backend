from db.db_conection import DataBase
from iam.models.userModel import User


class UserRepository:
    def __init__(self):
        self.database = DataBase()
        self.cursor = self.database.cursor
        self.connection = self.database.connection

    def find_user(self, username):
        sql = 'SELECT password FROM user WHERE username = "{0}";'.format(username)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            return user
        except Exception as e:
            print(e)

    def create_user(self, data: User):
        username = data['username']
        password = data['password']
        lastname = data['lastname']
        email = data['email']
        name = data['name']
        sql = 'insert into user (username, password, lastname, name, email) values ("{0}", "{1}", "{2}", "{3}", "{4}");'.format(username, password, lastname, name, email)
        try:
            result = self.cursor.execute(sql)
            self.connection.commit()
            return result
        except Exception as e:
            return e

    def close(self):
        self.connection.close()
