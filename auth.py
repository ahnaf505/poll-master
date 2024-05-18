from database import *
import random

def register_user(username, hashed_pswd):
    
    write_db("user_")