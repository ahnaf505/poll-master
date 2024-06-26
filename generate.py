import time
import random
import string
import os

usr_id_length = 29

def gen_user_id():
    unix_time = int(time.time())
    randint01 = random.randint(50, 50000)
    randint02 = random.randint(2, 50)
    randint03 = random.randint(20, 500)
    addd_numid = round(unix_time + randint01)
    divd_numid = round(addd_numid / randint02)
    multpld_numid = round(divd_numid * randint03)
    fnl_user_id = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + str(multpld_numid), k=usr_id_length))
    return str(fnl_user_id)

def gen_session_id():
    unix_time = int(time.time())
    load_avg = os.getloadavg()
    seed = int(sum(load_avg) * 1006)
    inttime = unix_time +seed
    fnl_sess_id = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + str(unix_time), k=usr_id_length))
    return str(fnl_sess_id)

