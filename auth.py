from database import *
from generate import *
import random

def register_user(username, hashed_pswd):
    rgstr_user_id = ""
    while True:
        curr_user_id = gen_user_id()
        if curr_user_id == read_db("user_id_"+curr_user_id):
            return
        else:
            rgstr_user_id = curr_user_id
            break
    write_db("user_id_"+rgstr_user_id, username)
    write_db("uid_username_"+username, hashed_pswd)