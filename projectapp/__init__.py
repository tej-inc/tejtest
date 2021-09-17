'''This file will import all the things we need in this package so that it will be accessible to any Blueprint (package) in the package'''
#the correct order

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

from projectapp.admin import adminobj
from projectapp.user import userobj

app = Flask(__name__,instance_relative_config=True)
csrfobj = CSRFProtect(app)

app.register_blueprint(adminobj)
app.register_blueprint(userobj)

from instance import config
app.config.from_pyfile("config.py")


db = SQLAlchemy(app)

from . import forms
from . import mymodels


