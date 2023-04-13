from iam.repository.user_repository import UserRepository
from iam.repository.role_repository import RoleRepository
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from iam.models.userModel import User


class UserService:
    def __init__(self):
        load_dotenv()
        self.userRepository = UserRepository()

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
        data['password'] = generate_password_hash(data['password'])
        result = self.userRepository.create_user(data)
        return result
