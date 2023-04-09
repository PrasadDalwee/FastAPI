import logging
import sys

def errorMsg(error):
    return {"Error":error}

def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print("--<> New Error Caught\n")
            print(errorMsg(str(e)),"\n")
            logging.exception(e)
            print("--<>\n \t\t\t ---\n")
            
    return inner_function
