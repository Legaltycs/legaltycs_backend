from iam.repository.role_repository import RoleRepository
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from iam.models.roleModel import Role

class RoleService:
    def __init__(self):
        load_dotenv()
        self.roleRepository = RoleRepository()

    def get_rol(self, roleName):
        try:
            result = self.roleRepository.find_role(roleName)
            if result is None:
                return False
            else:
                return result
        except Exception as e:
            print("Verify_role Error:", e)
            return False

    def register_role(self, data: Role):
        result = self.roleRepository.create_role(data)
        return result