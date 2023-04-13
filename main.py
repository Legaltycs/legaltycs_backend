from flask import Flask
from dotenv import load_dotenv
from routes.auth import routes_auth
from routes.private.test import routes_test
from iam.controllers.role_controller import routes_role
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(routes_auth, url_prefix="/api")
app.register_blueprint(routes_test, url_prefix="/api")
app.register_blueprint(routes_role, url_prefix="/api")
if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, port="4000", host="0.0.0.0")
