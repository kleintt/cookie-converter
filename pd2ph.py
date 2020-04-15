# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:33:25 2020

@author: Yongyao SUN
"""

import json

name = str(input('Please give the name of cookie file,like xxxx.json: \n'))
site = str(input('Please give the name of PH\'s website,like AdidasGB: \n'))
site_pd = str(
    input('Please give the name of PD\'s website,like adidas-gb(can be found in cookie file): \n'))
try:
    with open(name, 'r') as f:
        pd_cookie = json.load(f)
      
    ph_cookie = []
    for cookie in pd_cookie[site_pd]:
        tmp = {"cookie":cookie['cookie'],"site":site}
        ph_cookie.append(tmp)
        
    with open('ph_cookie.json', 'w') as f:
        json.dump(ph_cookie, f)
    print('完成')
except Exception as e:
     print("失败，exception {} ".format(e))
