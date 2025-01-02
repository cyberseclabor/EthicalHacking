!/usr/bin/env python

import requests
import dvwaData

session = requests.Session()

# Login to dvwa
url = dvwaData.dvwaAddr + '/dvwa/login.php'
postBody = {'username': 'admin', 'password': 'password', 'Login': 'Login'}
requestPost = session.post(url, postBody)

pages = open('pagesDvwa.txt').read().splitlines()

for page in pages:
    url = dvwaData.dvwaAddr + '/dvwa/' + page    
    response = session.get(url)
    
    if response.status_code == 200:
        print('[+] ---- ' + url + ' was found ----')
