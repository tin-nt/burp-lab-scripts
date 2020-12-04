#!/usr/bin/python3
#coding=utf-8

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>2FA bypass using a brute-force attack</title>
    </head>
    <body>
            <script src="/resources/js/labHeader.js"></script>
            
            <div id="academyLabHeader">
                <section class="academyLabBanner">
                    <div class="container">
                    <div class="logo"></div>
                        <div class="title-container">
                            <h2>2FA bypass using a brute-force attack</h2>
                            <a id='lab-link' class='button' href='/'>Back to lab home</a>
                            <a class="link-back" href="https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-bypass-using-a-brute-force-attack">
                                Back&nbsp;to&nbsp;lab&nbsp;description&nbsp;<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 28 30" enable-background="new 0 0 28 30" xml:space="preserve" title="back-arrow">
    <g>
        <polygon points="1.4,0 0,1.2 12.6,15 0,28.8 1.4,30 15.1,15"></polygon>
        <polygon points="14.3,0 12.9,1.2 25.6,15 12.9,28.8 14.3,30 28,15"></polygon>
    </g>
</svg>
                            </a>
                        </div>
                        <div class="widgetcontainer-lab-status is-notsolved">
                            <span>LAB</span>
                            <p>Not solved</p>
                            <span class="lab-status-icon"></span>
                        </div>
                    </div>
                </section>
            </div>

        <div theme="">
            <section class="maincontainer">
                <div class="container is-page">
                    <header class="navigation-header">
                        <section class="top-links">
                            <a href=/>Home</a><p>|</p>
                            <a href="/login">Login</a><p>|</p>
                        </section>
                    </header>
                    <header class="notification-header">
                    </header>
                    <h1>Login</h1>
                    <section>
                        <p class=is-warning>Incorrect security code</p>
                        <form class=login-form method=POST action=/login>
                            <input required type="hidden" name="csrf" value="PBBgOzaN0WuoKGsFZXm4caHFblhqdSyM">
                            <label>Username</label>
                            <input required type=username name="username">
                            <label>Password</label>
                            <input required type=password name="password">
                            <button class=button type=submit> Log in </button>
                        </form>
                    </section>
                </div>
            </section>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup)
print(soup.find_all("p","is-warning"))