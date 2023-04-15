import time
import jwt
from decouple import config

#decouple accesses .ini and .env files and config helps to plug variables stored in them
JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

print(JWT_SECRET, JWT_ALGORITHM)


#returns generated tokens
def token_response(token: str):
    return {
        "access token" : token
    }

#function to encode and sign with jwt token
def signJWT(userID : str):
    payload= {
        "userID" : userID,
        "expires" : time.time() + 600000 #600,000ms->600sec->10min expiry
    }

    token= jwt.encode(payload=payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM).decode('utf-8')
    return token_response(token)

#function to decode encoded JWT string
def decodeJWT(token:str) -> dict:
    decode_token=jwt.decode(jwt=token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
    print(decode_token)
    return decode_token if decode_token['expires'] >= time.time() else None
    
    
# tok=signJWT("kadu@gmail.com")
# decodeJWT(tok)