from flask import Blueprint, request
from function_jwt import validate_token
from flask import jsonify

routes_test = Blueprint("routes_test", __name__)


@routes_test.before_request
def verify_token_middelware():
    try:
        token = request.headers['Authorization'].split(" ")[1]
    except Exception as e:
        response = jsonify({"menssage": "Token is required " + str(e)})
        response.status_code = 404
        return response
    return validate_token(token, output=False)


@routes_test.route("/test", methods=["GET"])
def test():
    data = request.get_json()
    return data
