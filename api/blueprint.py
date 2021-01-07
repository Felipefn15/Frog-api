from flask import Blueprint
from flask_restful import Api
from .order import Order

def setup_blueprint():
    blueprint = Blueprint(
        "products", __name__,
    )

    api = Api(blueprint)
    api.add_resource(Order, "/order")
    return blueprint