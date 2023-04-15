from pydantic import BaseModel, Field, EmailStr 

class Schema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "title": "Securing FastAPI applications with JWT.",
            }
        }
        

class db:
    data=[]
    

def func(userDB: db, userData: Schema):
    userDB.data.append(userData)
    
userDB=db()
func(userDB, Schema(id=1, title='PND'))
print(userDB.data)