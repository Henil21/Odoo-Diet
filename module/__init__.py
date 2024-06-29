from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_DATABASE_MODIFICATIONS'] = False
app.secret_key = 'asdfgh'

from module import *
from .model import *

from .app import *