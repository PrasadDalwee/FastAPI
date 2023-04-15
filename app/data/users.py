from app.model import UserSchema


class userDB:
    data=[]

    def append(self, data: UserSchema):
        self.data.append(data)
    
    def showData(self):
        return self.data
