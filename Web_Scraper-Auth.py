#
# import requests
import getpass
# from bs4 import BeautifulSoup

mypass = getpass.getpass("Enter your password: ")

header = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

login_data = {
	'username': 'th596u',
	'password': 'mypass'
}

# url = 'https://oidc.idp.elogin.att.com/mga/sps/authsvc?PolicyId=urn:ibm:security:authentication:asf:pass'
# s = requests.Session()
# data = s.get(url, headers = header)

# print(data)
print(login_data)
# s.close()