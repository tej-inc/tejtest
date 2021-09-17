from flask import Blueprint

userobj = Blueprint('bpuser',__name__,template_folder='templates',static_folder='static')

from . import userroutes


