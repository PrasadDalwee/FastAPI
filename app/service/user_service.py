from app.data.users import userDB
from app.model import UserLoginSchema, UserSchema


def user_exist(users: userDB, email: str):
    for user in users.data:
        if(user.email==email):
            return True
    return False

def user_signUp(users: userDB, data: UserSchema):
    users.append(data)

def user_LogIn(users: userDB, data: UserLoginSchema):
    for user in users.data:
        if user.email==data.email:
            if user.password==data.password:
                return True
            else:
                return False
    return False

