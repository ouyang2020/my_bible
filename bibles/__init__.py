from flask import Flask,render_template
from flask_bcrypt import Bcrypt

#bcrypt = Bcrypt()
#login_manager = LoginManager()


def create_app():
    app = Flask(__name__,template_folder="templates")

    from bibles.routers import main
    app.register_blueprint(main)

    return app