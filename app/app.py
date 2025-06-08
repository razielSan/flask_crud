from flask import Flask
import secrets

from views import (
    index_app,
    examples_app,
    clicker_app,
    products_app,
)
from csrf_protection import csrf_protect


def create_app():
    app = Flask(__name__)
    csrf_protect.init_app(app)

    app.config.update(
        TEMPLATE_AUTO_RELOAD=True,
        SECRET_KEY=secrets.token_hex(),
    )
    app.register_blueprint(index_app)
    app.register_blueprint(examples_app, url_prefix="/examples")
    app.register_blueprint(clicker_app, url_prefix="/clicker")
    app.register_blueprint(products_app, url_prefix="/products")
    return app
