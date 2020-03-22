import pymongo
from mongoengine import *
from passwordmaker_pkg import PasswordMaker

maker = PasswordMaker.PasswordMaker()

print(maker.create_password())
