import os
import platform
from flask import Flask
from datetime import timedelta

from app.controller import distance_route


def create_app():
    template_dir = os.getcwd() + ('\\app\\views' if platform.system() == 'Windows' else '/app/views')
    application = Flask(__name__, template_folder=template_dir)
    application.config['SECRET_KEY'] = "pbkdf2:sha256:150000$7386R9s5$a14bac70f0c6846c3db96dcda57fce3ab24c049d4f6ac70ddc1fa549a52f3c88"
    application.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
    application.register_blueprint(distance_route)
    
    return application
