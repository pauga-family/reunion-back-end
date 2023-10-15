from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# # Avoid circular dependencies byimporting here
# from app.User import bp as user_bp
# app.register_blueprint(user_bp, url_prefix='/user')

# from app import routes, models

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate = Migrate(app, db)

    #Avoid circular dependencies byimporting here
    from app.User import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    return app