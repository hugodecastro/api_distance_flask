from flask import Blueprint


# Register route for <nutricionista> controller
from app.controller.distance_controller import *
distance_route = Blueprint('distance', __name__, template_folder='templates')
distance_route.add_url_rule('/distance/doc', view_func=doc, methods=['GET'])
distance_route.add_url_rule('/distance/g/<destination>', view_func=index, methods=['GET'])
