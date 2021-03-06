from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')
    app.secret_key = os.getenv("SECRET_KEY", 'iU9GW39Ghs2Jh1Rq0n0Pn8AwIsiXnwB9')

    db.init_app(app)

    return app


app = create_app()