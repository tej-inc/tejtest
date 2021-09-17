import os
from instance.config import SECRET_KEY
from flask import Flask
from flask import render_template,abort , make_response,request,redirect,flash
from flask.helpers import get_flashed_messages
from flask_wtf.csrf import CSRFProtect 
from forms import login,register
app = Flask(__name__,instance_relative_config=True)
csrfobj = CSRFProtect(app)
app.config.from_pyfile("config.py")




@app.errorhandler(404)
def fatalerror(error):
    return (render_template('error.html',error=error),404)



if __name__=='__main__':
    #app.config['DEBUG']=True
    #app.config['PORT'] = 8088
    app.config['SECRET_KEY']=SECRET_KEY
    app.run()