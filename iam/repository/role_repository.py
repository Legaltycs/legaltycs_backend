from db.db_conection import DataBase
from iam.models.roleModel import Role
import uuid

class RoleRepository: 
    def __init__(self):
        self.database = DataBase()
        self.cursor = self.database.cursor
        self.connection = self.database.connection
    
    def find_role(self, roleName):
        sql = 'SELECT id FROM role WHERE roleName = "{0}";'.format(roleName)
        try:
            self.cursor.execute(sql)
            role = self.cursor.fetchone()
            return role
        except Exception as e:
            print(e)

    def create_role(self, data: Role):
        roleName = data['roleName']
        id = uuid.uuid4()
        sql = 'insert into role (id, roleName) values ("{0}", "{1}");'.format(id, roleName)
        try:
            result = self.cursor.execute(sql)
            self.connection.commit()
            return result
        except Exception as e:
            return e