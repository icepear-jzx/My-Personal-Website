import os

from flask import Flask, redirect, url_for


def create_app():

    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello():
        return redirect(url_for('home.index'))

    from . import db

    from . import auth
    app.register_blueprint(auth.bp)

    from . import home
    app.register_blueprint(home.bp)

    from . import skills
    app.register_blueprint(skills.bp)

    from . import projects
    app.register_blueprint(projects.bp)

    return app
