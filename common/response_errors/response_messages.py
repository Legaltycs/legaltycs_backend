from flask import jsonify

def status_ok () : 
    response = jsonify ({ "message" : "Usuario registrado correctamente" })
    response.status_code = 200
    return response

def status_bad_request (message) : 
    response = jsonify ({ "message" : message })
    response.status_code = 400
    return response

