import os

import stripe
from flask import Flask, jsonify, render_template

from .services import create_customer

stripe_keys = {
    "secret_key": os.environ["STRIPE_SECRET_KEY"],
    "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
}
stripe.api_key = stripe_keys["secret_key"]


# https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/

def create_app(config_filename=None):
    app = Flask(__name__)
    if config_filename:
        app.config.from_pyfile(config_filename)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/call-stripe")
    @app.route("/call-stripe/<name>")
    def call_stripe(name=None):
        customer = create_customer(name)
        print(customer)
        return jsonify(customer)

    return app


app = create_app()
