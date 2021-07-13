from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Password123!@34.142.111.19/example_db"

db = SQLAlchemy(app)

from application import routes