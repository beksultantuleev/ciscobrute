
from src.brute_test_core import *
from raw_data.credentials import *

result = attack(target=target, usernames=username,
        passwords=passwd, groups=groups, rate=1)
print(result)