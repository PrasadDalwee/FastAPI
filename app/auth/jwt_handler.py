import time
import jwt
from decouple import config

#decouple accesses .ini and .env files and config helps to plug variables stored in them
JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


#returns generated tokens
def token_response(token: str):
    return {
        "access token" : token
    }

#function to encode and sign with jwt token
def signJWT(userID : str):
    payload= {
        "userID" : userID,
        "expiry" : time.time() + 600 #600ms expiry
    }

    token= jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token_response(token)

#function to decode encoded JWT string
def decodeJWT(token:str):
    decode_token=jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return decode_token if decode_token['expires'] >= time.time() else None

