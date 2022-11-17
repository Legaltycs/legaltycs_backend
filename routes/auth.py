from flask import Blueprint, request, jsonify
from function_jwt import write_token
from services.user_services import UserService

userService = UserService()
routes_auth = Blueprint("routes_auth", __name__)


@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    verified_user = userService.verify_user(data['username'], data['password'])
    userResource = {
            'username': data['username']
    }
    if verified_user:
        token = write_token(data=userResource)
        response = jsonify({"token": token.decode('utf-8')})
        response.status_code = 200
        return response
    else:
        response = jsonify({"menssage": "User or password not valid"})
        response.status_code = 404
        return response


@routes_auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    result = userService.register_user(data)
    if result:
        response = jsonify({"menssage": "Username already exist"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"menssage": "User successfully registered"})
        response.status_code = 200
        return response
