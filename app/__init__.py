from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from app.resources.store import StoreList, Store
from app.security.security import identity, authenticate
from app.resources.user import UserRegister
from app.resources.items import Items, ItemList
from app.database.db import db

# this __init__ file basically lets one import files
app = Flask(__name__)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

app.secret_key = "top_secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)
jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)

api.add_resource(Items, "/items/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/signup")
api.add_resource(Store, "/stores/<string:name>")
api.add_resource(StoreList, "/stores")
