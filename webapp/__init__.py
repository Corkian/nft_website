from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from webapp.config import Config
from flask_bootstrap import Bootstrap
from flask_talisman import Talisman

db = SQLAlchemy()
mail = Mail()


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    bootstrap = Bootstrap(app)
    db.init_app(app)
    mail.init_app(app)
    Talisman(app, content_security_policy=None)

    from webapp.main.routes import main_bp

    app.register_blueprint(main_bp)

    return app
