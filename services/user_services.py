from repository.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from models.userModel import User


class UserService:
    def __init__(self):
        load_dotenv()
        self.userRepository = UserRepository()

    def verify_user(self, name, password):
        result = self.userRepository.find_user(name, password)
        if check_password_hash(result[1], password):
            return True
        else:
            return False

    def register_user(self, data: User):
        data['password'] = generate_password_hash(data['password'])
        self.userRepository.create_user(data)
