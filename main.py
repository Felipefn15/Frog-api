import os
from flask import Flask
from flask_cors import CORS
from api import setup_blueprint as blueprint


app = Flask(__name__)

CORS(app)


def _register_blueprints(app):
    print("Registering blueprints")
    app.register_blueprint(blueprint())

def start_app(app):
    _start_services()
    _register_blueprints(app)


def run_server():
    port = int(os.environ.get("PORT", 5000))

    _register_blueprints(app)

    app.run(host='127.0.0.1', port=port)

run_server()