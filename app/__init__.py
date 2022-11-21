import logging
import warnings

from flask import Flask, session
from flask_babel import Babel
from flask_mailing import Mail
from flask_sqlalchemy import SQLAlchemy
from sassutils.wsgi import SassMiddleware

from flask_session import Session

babel = Babel()
mail = Mail()
sess = Session()
db = SQLAlchemy()


def create_app(config_object: str = "ProdConfig") -> Flask:
    """Create an application with the given configuration class.

    Args:
        config_object (str, optional): Config class from "config.py". Defaults to "DevConfig".

    Returns:
        app: flask application
    """
    app = Flask(__name__)

    with warnings.catch_warnings():
        # Ignore the below warning from `SassMiddleware`.
        # FutureWarning: `strip_extension` was not specified, defaulting to `False`
        warnings.simplefilter(action="ignore", category=FutureWarning)

        # Register scss middleware.
        app.wsgi_app = SassMiddleware(
            app.wsgi_app,
            {"app": ("static/scss", "static/css", "/static/css")},
        )

    # Use given configuration object.
    app.config.from_object(f"config.{config_object}")

    babel.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    sess.init_app(app)

    # Register blueprints.
    from app.error import error_bp
    from app.main import main_bp

    app.register_blueprint(error_bp)
    app.register_blueprint(main_bp)

    @babel.localeselector
    def get_locale():
        # If the user has set up the language manually it will be stored in the session,
        # so we use the locale from the user settings.
        return session.get("language", "en")

    return app
