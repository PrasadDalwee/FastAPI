from fastapi import Body, FastAPI, Depends
from app.auth.jwt_handler import signJWT
from app.data.users import userDB
from app.exceptions.error import errorMsg, exception_handler
from app.model import PostSchema, UserLoginSchema, UserSchema
from app.service.user_service import user_LogIn, user_exist, user_signUp
from app.auth.jwt_bearer import jwtBearer
#creating FastAPI's webapp
app=FastAPI()

#Substituting DB
posts= [
    {
        "id":1, 
        "title" : "Penguin",
        "content": "Antartica Maybe"
    }
]

usersDB = userDB()

# 1.landing page
@app.get("/")
def root():
    return "use /docs to view APIs"

# 2. Creating a GET request for testing
@exception_handler
@app.get("/get", tags=["testing"])
def root():
    return {"API":"FastAPI"}

# 3. GET all posts
@exception_handler
@app.get("/posts",tags=["search posts"])
def get_posts():
    return {"data" : posts}

# 4. GET post by id
@exception_handler
@app.get("/posts/{id}", tags=["search posts"])
def get_post_by_id(id:int):
    if id>len(posts):
        return errorMsg("Post with this id doesn't exist")

    for post in posts:
        if post["id"]==id:
            return {"data": post}    
    
    return errorMsg("Post with this id doesn't exist")

# 5. POST a post
@exception_handler
@app.post("/addPost", tags=["create posts"],dependencies=[Depends(jwtBearer())])
def createPost(post:PostSchema):
    post.id=len(posts)+1
    posts.append(post.dict())
    return {"info":"Post created successfully"} 

# 6. POST user SignUp
@exception_handler
@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema=Body()):
    if user_exist(usersDB,user.email):
        return errorMsg("User already exists.")
    else:
        user_signUp(usersDB,user)
        return signJWT(user.email)
    

# 7. POST user LogIn
@exception_handler
@app.post("/user/login",tags=["user"])
def user_login(user: UserLoginSchema):
    if user_exist(userDB,user.email):
        if user_LogIn(userDB,user):
            return signJWT(user.email)
        else:
            return errorMsg("Wrong Password.")
    return errorMsg("User doesn't exists.")

# 8. GET all user data
@exception_handler
@app.get("/user/showUsers", tags=["user"])
def user_display_all():
    return usersDB.showData()