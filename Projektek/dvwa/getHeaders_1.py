#!/usr/bin/env python

import requests
import dvwaData

response = requests.get(dvwaData.dvwaAddr + '/dvwa/login.php')

print(response.headers)
