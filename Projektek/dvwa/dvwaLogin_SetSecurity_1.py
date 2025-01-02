#!/usr/bin/env python

import requests
import dvwaData

session = requests.Session()

# Login to dvwa
url = dvwaData.dvwaAddr + '/dvwa/login.php'
postBody = {'username': 'admin', 'password': 'password', 'Login': 'Login'}
requestPost = session.post(url, postBody)

print(requestPost)


# Modify the security level - set to low
url = dvwaData.dvwaAddr + '/dvwa/security.php'
postBody = {'security': 'low', 'seclev_submit': 'seclev_submit'}
requestPost = session.post(url, postBody)

print(session.cookies.get_dict())

print(requestPost)
