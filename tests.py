from auth import *

print(register_user("ahnaf", "aaanaf"))
sess = login_user("ahnaf", "aaanaf")
time.sleep(10)
print(action(sess))