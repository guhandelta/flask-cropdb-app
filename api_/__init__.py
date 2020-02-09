from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)  # create the Flask app

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

    db.init_app(app)

    # Importing here preventes any circular inputs and importing is done after the Flask app has been created
    from .views import main
    app.register_blueprint(main)

    return app
