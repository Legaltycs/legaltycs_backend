from iam.repository.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from iam.models.userModel import User
from iam.services.role_services import RoleService


class UserService:
    def __init__(self):
        load_dotenv()
        self.userRepository = UserRepository()
        self.roleService = RoleService()

    def verify_user(self, name, password):
        try:
            result = self.userRepository.find_user(name)
            if result is None:
                return False
            if check_password_hash(result[0], password):
                return result
            else:
                return False
        except Exception as e:
            print("Verify_user Error:", e)
            return False

    def register_user(self, data: User):
        role = self.roleService.get_rol(data['roleName'])
        data['password'] = generate_password_hash(data['password'])
        data.update({'role_id': role[0]})
        result = self.userRepository.create_user(data)
        return result
