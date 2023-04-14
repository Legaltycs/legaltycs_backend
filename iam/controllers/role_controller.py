from iam.services.role_services import RoleService
from flask import Blueprint, request, jsonify

roleService = RoleService()
routes_role = Blueprint("routes_role", __name__)


@routes_role.route("/role", methods=["POST"])
def create_role():
   try:
      data = request.get_json()
      result = roleService.register_role(data)
      if result != 1:
          response = jsonify({"message": "El rol ya existe"})
          response.status_code = 400
          return response
      else:
          response = jsonify({"message": "Rol creado correctamente"})
          response.status_code = 200
          return response
   except Exception as e:
       response = jsonify({"message": e})
       response.status_code = 500
       return response