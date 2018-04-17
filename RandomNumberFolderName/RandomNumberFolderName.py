#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import platform
import random
import os
strtnmbr=int(input("Start Number:"))
fnshnmbr=int(input("Finish Number:"))
sayi=random.randrange(strtnmbr,fnshnmbr)
if platform=="linux":
    os.system("mkdir "+sayi.__str__())
    input("OK")
elif platform=="win32":
    os.system("md "+sayi.__str__())
    input("OK")
else:
    input("Unsupported System Version")








