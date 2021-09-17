from flask import render_template,make_response,abort,request,redirect,flash,session
from . import adminobj
from projectapp.forms import login,register





@adminobj.route('/admin')
def mainpage():
    return render_template('index.html')

@adminobj.route('/logout')
def logout():
    if session.get('user')!=None:
        session.pop('user')
        return render_template('upage1.html')


@adminobj.errorhandler(404)
def fatalerror(error):
    return (render_template('error.html',error=error),404)

