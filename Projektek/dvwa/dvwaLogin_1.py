#!/usr/bin/env python

# Belépés a Metasploitable 2 VM-n lévő dvwa alkalmazásba
import requests
import dvwaData

session = requests.Session()

# Login to dvwa
url = dvwaData.dvwaAddr + '/dvwa/login.php'
postBody = {'username': 'admin', 'password': 'password', 'Login': 'Login'}
requestPost = session.post(url, postBody)

print(requestPost)
