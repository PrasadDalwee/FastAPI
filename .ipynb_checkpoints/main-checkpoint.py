from fastapi import FastAPI

#creating FastAPI's webapp
app=FastAPI()

#Creating a GET request
@app.get("/get")
def root():
    return {"API":"FastAPI"}