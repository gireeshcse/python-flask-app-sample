import os

from flask import Flask, request, redirect, Response, current_app
import requests
import json

def create_app(test_config=None):
    # create and configure the app
    # __name__ is the name of the current python module
    # instance_relative_config tells the app the configuration files are relative to the instance folder
    # the instance folder is located outside the samchitam package and can hold local data that should't be
    # committed to version control such as configuration secrets and the database file
    app = Flask(__name__, instance_relative_config=True,static_url_path='/')

    # sets some default configuration that the app will use
    app.config.from_mapping(
        SECRET_KEY = 'dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('settings.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return "Welcome to " + current_app.config['APP_NAME']

    @app.errorhandler(404)
    def not_found(e):
        return "Welcome to " + current_app.config['APP_NAME'] + " - Invalid URL 404"

    return app