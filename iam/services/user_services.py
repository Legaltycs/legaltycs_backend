from iam.repository.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from iam.models.userModel import User
from iam.services.role_services import RoleService
from common.response_errors.response_errors import status_bad_request, status_ok

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
        
        if not data.get('roleName', 0) : 
            return status_bad_request('El rol es requerido')
        role = self.roleService.get_rol(data['roleName'])
        if not role:
            return status_bad_request('El rol no existe')
        
        data['password'] = generate_password_hash(data['password'])
        data.update({'role_id': role[0]})
        result = self.userRepository.create_user(data)
        print ("result", result)
        if result != 1:
            return status_bad_request('El usuario y/o email ya existe')
        return status_ok()
