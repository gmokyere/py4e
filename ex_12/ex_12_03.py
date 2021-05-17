# -*- coding: utf-8 -*-
print("Hello welcome to Ex 13\n")

import urllib.request
import ssl


""" Ex_13_03 """

## Use to read https and http
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

## Open file directly from wepage
fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt', context = ctx)

## Show the first 3000 characters
print(fhand.read(3000).decode())
