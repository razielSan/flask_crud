from flask import Flask

from views import index_app, examples_app, clicker_app


def create_app():
    app = Flask(__name__)
    app.config.update(
        TEMPLATE_AUTO_RELOAD=True,
    )
    app.register_blueprint(index_app)
    app.register_blueprint(examples_app, url_prefix="/examples")
    app.register_blueprint(clicker_app, url_prefix="/clicker")
    return app
