from repository.user_repository import UserRepository
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
from models.userModel import User


class UserService:
    def __init__(self):
        load_dotenv()
        self.userRepository = UserRepository()

    def verify_user(self, name, password):
        encripted_pass = generate_password_hash(password)
        print(encripted_pass)
        result = self.userRepository.find_user(name, encripted_pass)
        if result > 0:
            return True
        else:
            return False

    def register_user(self, data: User):
        data['password'] = generate_password_hash(data['password'])
        self.userRepository.create_user(data)
