from flask import Flask
from flask_cors import CORS
from src.routes.worker_routes import bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(bp, url_prefix="/api/worker")
    return app
