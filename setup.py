'''This module starts the server and that is it's only function'''
from projectapp import app 


if __name__=='__main__':
    app.run(debug=True,port=5000) 

