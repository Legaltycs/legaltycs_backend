from flask import Blueprint, request, jsonify
from function_jwt import write_token
from iam.services.user_services import UserService

userService = UserService()
routes_auth = Blueprint("routes_auth", __name__)


@routes_auth.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        verified_user = userService.verify_user(data['username'], data['password'])
        if verified_user:
            userResource = {
                    'username': data['username']
            }
            token = write_token(data=userResource)
            response = jsonify({"id": verified_user[1], "token": token.decode('utf-8')})
            response.status_code = 200
            return response
        else:
            response = jsonify({"message": "User or password not valid"})
            response.status_code = 400
            return response
    except Exception as e:
        response = jsonify({"message": e})
        response.status_code = 500
        return response


@routes_auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    result = userService.register_user(data)
    print("regiter endpoint", result)
    if result != 1:
        response = jsonify({"message": "Username and email already exist"})
        response.status_code = 400
        return response
    else:
        response = jsonify({"message": "User successfully registered"})
        response.status_code = 200
        return response
