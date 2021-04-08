import sqlite3
from flask_restful import Resource, reqparse

# Have to insert null in as id is autoincrementing
from app.models.user_model import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="password field cannot be blank")
    parser.add_argument('password', type=str, required=True, help="username field cannot be blank")

    def post(self):
        data = UserRegister.parser.parse_args()
        item = UserModel.find_by_username(data["username"])
        if item:
            return {"message": "username already exists"}, 400

        user = UserModel(**data)
        user.save()
        return {"message": "user created successfully"}
