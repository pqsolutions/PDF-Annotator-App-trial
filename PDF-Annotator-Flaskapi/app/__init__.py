# app/__init__.py
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.api_service.fields_api import fields_api
app.register_blueprint(fields_api, url_prefix='/fields')

from app.api_service.files_api import files_api
app.register_blueprint(files_api, url_prefix='/files')