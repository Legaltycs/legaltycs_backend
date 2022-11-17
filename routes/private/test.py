from flask import Blueprint, request
from middelware.token_middelware import verify_token_middelware

routes_test = Blueprint("routes_test", __name__)


@routes_test.route("/test", methods=["GET"])
@verify_token_middelware
def test():
    data = request.get_json()
    return data
