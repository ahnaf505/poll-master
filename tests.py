from auth import *

sess = login_user("ahnaf", "aaanaf")
time.sleep(4)
print(action(sess))
time.sleep(6)
print(action(sess))