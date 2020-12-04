#!/usr/bin/python3
#coding=utf-8
from base64 import encode
import base64
import hashlib
import os

with open("/opt/fuzzdb/wordlists-user-passwd/auth-pass.txt") as f:
    line = f.readline()
    fp = open('encoded-password.txt','w')
    while line:
        result = hashlib.md5(line.strip().encode('utf-8')).hexdigest()
        result = 'carlos:'+str(result)
        # result = base64.b64encode(result.encode('utf-8'))
        print(result.decode('utf-8')) #debug
        fp.write(result.decode('utf-8') + '\n')
        line = f.readline()

    fp.close()    
    