from fastapi import FastAPI
from app.exceptions.error import errorMsg
from app.model import PostSchema

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

users = []

#landing page
@app.get("/")
def root():
    return "use /docs to view APIs"

#Creating a GET request for testing
@app.get("/get", tags=["testing"])
def root():
    return {"API":"FastAPI"}

#GET all posts
@app.get("/posts",tags=["search posts"])
def get_posts():
    return {"data" : posts}

#GET post by id
@app.get("/posts/{id}", tags=["search posts"])
def get_post_by_id(id:int):
    if id>len(posts):
        return errorMsg("Post with this id doesn't exist")

    for post in posts:
        if post["id"]==id:
            return {"data": post}    
    
    return errorMsg("Post with this id doesn't exist")

#POST a post
@app.post("/addPost", tags=["create posts"])
def createPost(post:PostSchema):
    post.id=len(posts)+1
    posts.append(post.dict())
    return {"info":"Post created successfully"} 
