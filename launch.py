
from src.brute_test_core import *
from raw_data.credentials import *
target = check_target(target)

# print(ssl.OPENSSL_VERSION)
print(target)
result = attack(target=target, usernames=username,
        passwords=passwd, groups=groups, rate=5)
print(result)


