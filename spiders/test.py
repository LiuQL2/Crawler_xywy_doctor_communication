# -*- coding:utf-8 -*-
import base64
import urllib2

proxy_handler = urllib2.ProxyHandler({'http': '23.106.159.52:3128'})
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
proxy_auth_handler = urllib2.ProxyBasicAuthHandler(password_mgr)
proxy_auth_handler.add_password(None, '23.106.159.52:3128', 'longer', 'longer')

opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
urllib2.install_opener(opener)

url ='http://www.google.com'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()