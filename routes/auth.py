from flask import Blueprint, request, jsonify
from function_jwt import write_token
from db.db_conection import DataBase

routes_auth = Blueprint("routes_auth", __name__)


@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    database = DataBase()
    print(database)
    if data['username'] == "Nelson Hernandez":
        return write_token(data=request.get_json())
    else:
        response = jsonify({"menssage": "User not found"})
        response.status_code = 404
        return response
