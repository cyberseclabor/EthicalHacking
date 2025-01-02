#!/usr/bin/env python

import requests
import dvwaData

response = requests.get(dvwaData.dvwaAddr)

print(response.content)
