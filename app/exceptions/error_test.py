#from app.exceptions.error import exception_handler
from error import exception_handler

@exception_handler
def errorfunc(a):
    s=a/0
    return "done"

errorfunc("hello")
errorfunc(20)
print("something is still cooking.....")