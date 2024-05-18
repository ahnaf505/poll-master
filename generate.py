import time
import random
import math
import string

usr_id_length = 29

def gen_user_id():
    unix_time = int(time.time())
    randint01 = random.randint(50, 50000)
    randint02 = random.randint(2, 50)
    randint03 = random.randint(20, 500)
    addd_numid = math.round(unix_time + randint01)
    divd_numid = math.round(addd_numid / randint02)
    multpld_numid = math.round(divd_numid * randint03)
    fnl_user_id = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + multpld_numid, k=usr_id_length))
    return str(fnl_user_id)
