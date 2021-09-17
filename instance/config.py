from os import environ,path,urandom
import os
from dotenv import load_dotenv


basedir=path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,' .env'))
SECRET_KEY= os.urandom(32)
from os import environ,path
SQLALCHEMY_DATABASE_URI= 'mysql+mysqlconnector://root@localhost/tej'
SQLALCHEMY_TRACK_MODIFICATIONS=True
