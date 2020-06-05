 # -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:15:49 2018

@author: acer
"""

import urllib.request, re
while 1:
    n=input('-->> ')
    f=urllib.request.urlopen(n)
    s=f.read().decode('utf-8')
    print(re.findall(r"\+\d{2}\s?0?\d{10}",s))
    print(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s))


#import re
#from urllib.request import Request, urlopen
#url="https://www.youtube.com/user/Haciproductionss"
#req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#
#web_byte = urlopen(req).read()
#
#webpage = web_byte.decode('utf-8')
#print(re.findall(r"\+\d{2}\s?0?\d{10}",webpage))
#print(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",webpage))



