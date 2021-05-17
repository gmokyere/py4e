# -*- coding: utf-8 -*-
"""
Spyder Editor

ex_09
"""
import urllib.request
import ssl
print("Hello welcome to Ex 13\n")

from bs4 import BeautifulSoup

""" Ex_13_04 """

## Use to read https and http
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

## Open file directly from wepage
url = input("Enter url -")
fhand = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(fhand, "html.parser")

## Retrieve all paragraphs
ptags = soup('p') ## this returns a list of all ps

print("There were", len(ptags), "paragraphs")



    
