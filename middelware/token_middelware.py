from function_jwt import validate_token
from flask import jsonify, request
from functools import wraps


def verify_token_middelware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            token = request.headers['Authorization'].split(" ")[1]
        except Exception as e:
            response = jsonify({"menssage": "Token is required " + str(e)})
            response.status_code = 404
            return response
        response = validate_token(token, output=False)
        if response:
            return response
        else:
            return func(*args, **kwargs)

    return decorated_function
