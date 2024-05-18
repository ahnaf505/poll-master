import time
import random

def gen_user_id():
    unix_time = int(time.time())
    randint01 = random.randint(50, 50000)
    addd_numid = unix_time + randint01
