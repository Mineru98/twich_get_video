# -*- coding:utf-8 -*-
import requests

for id in range(0, 2150):
    res = requests.get('https://d1m7jfoe9zdc1j.cloudfront.net/68ec662706099491e179_lck_korea_42255849053_1623050996/chunked/{}.ts'.format(id))
    if res.status_code != 403:
        with open("../source/"+str('{}.ts'.format(str(id).zfill(4))), 'wb') as f:
            f.write(res.content)