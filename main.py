from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from py4j.java_gateway import JavaGateway
from routes.auth import routes_auth
from routes.private.test import routes_test
from routes.search import search_routes


app = Flask(__name__)

#Conexion con Protegé
gateway = JavaGateway()
ontology = gateway.entry_point.getOntology()

CORS(app, resources={r"/api/*": {"origins": "*"}})

# Registrar rutas
app.register_blueprint(search_routes)
app.register_blueprint(routes_auth, url_prefix="/api")
app.register_blueprint(routes_test, url_prefix="/api")

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, port="4000", host="0.0.0.0")
