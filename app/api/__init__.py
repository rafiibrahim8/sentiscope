from flask import Blueprint

from .v1 import get_blueprint as get_v1_blueprint

api = Blueprint('api', __name__, url_prefix='/api')
api.register_blueprint(get_v1_blueprint())


def get_blueprint():
    return api
