from database import *
from generate import *

def register_user(username, hashed_pswd):
    rgstr_user_id = ""
    while True:
        curr_user_id = gen_user_id()
        if curr_user_id == read_db("user_id_"+curr_user_id):
            return
        else:
            rgstr_user_id = curr_user_id
            break
    write_db("user_usn_"+username, rgstr_user_id)
    write_db("user_uid_"+rgstr_user_id, hashed_pswd)
    return rgstr_user_id

def login_user(username, hashed_pswd):
    isuser = read_db("user_usn_"+username)
    if isuser != None:
        corr_pswd = read_db("user_uid_"+isuser)
        if corr_pswd == hashed_pswd:
            start_time = time.time()
            fnl_sess_id = ""
            while True:
                curr_sess_id = gen_session_id
                if curr_sess_id == read_db("user_session_"+curr_sess_id):
                    return
                else:
                    fnl_sess_id = curr_sess_id
                    break
            write_db("user_session_"+fnl_sess_id)
            return fnl_sess_id
    else:
        return None

# while time.time() - start_time < LOGIN_TIMEOUT: