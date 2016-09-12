#!/usr/bin/env python3

import requests
import json
import yaml
import os

path = os.path.join(os.path.expanduser("~"), '.lb','lb.yaml')
with open(path) as stream:
    cfg = yaml.load(stream)

info = cfg['repos']['github']
url  = 'https://api.github.com/repos/{}/{}/releases/latest'.format(
    info['user'],
    info['repo'])

req = requests.get(url)
res = json.loads(req.text)
dwl = next((x for x in res['assets'] if x['name'].startswith(info['name'])))

print(dwl['browser_download_url'])
