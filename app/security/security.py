from werkzeug.security import safe_str_cmp
from app.models.user_model import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
    return None

def identity(payload):
    user_id = payload['identity']
    print(payload)
    return UserModel.find_by_id(user_id)
