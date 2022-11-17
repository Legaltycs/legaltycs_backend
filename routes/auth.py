from flask import Blueprint, request, jsonify
from function_jwt import write_token
from services.user_services import UserService

userService = UserService()
routes_auth = Blueprint("routes_auth", __name__)


@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    verified_user = userService.verify_user(data['username'], data['password'])
    if verified_user:
        return write_token(data=request.get_json())
    else:
        response = jsonify({"menssage": "User not found"})
        response.status_code = 404
        return response


@routes_auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    userService.register_user(data)
    return data
