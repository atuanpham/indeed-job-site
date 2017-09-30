from flask import Flask, redirect, url_for
from flaskext.markdown import Markdown
import os

app = Flask(__name__)
Markdown(app)

# configurations
try:
    app.config.from_object(os.environ['APP_SETTINGS'])
except KeyError:
    app.config.from_object('config.DevelopmentConfig')

from components.public.controllers import public_blueprint

# Register blueprints
app.register_blueprint(public_blueprint, url_prefix='/jobs')


@app.route('/')
def index():
    return redirect(url_for('public.home'))

