"""Init module
"""
from flask import Flask

from configuration.env import Env

app = Flask(__name__)
app.config.from_object(Env)

from website import views
