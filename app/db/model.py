import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
base_path = os.path.dirname(__file__)
database_name = "main.db"
database_path = os.path.join(base_path, "../../", database_name)


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


