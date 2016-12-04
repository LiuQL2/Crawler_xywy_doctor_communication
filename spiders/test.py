# -*- coding:utf-8 -*-
# import base64
# import urllib2
#
# proxy_handler = urllib2.ProxyHandler({'http': '23.106.159.52:3128'})
# password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
# proxy_auth_handler = urllib2.ProxyBasicAuthHandler(password_mgr)
# proxy_auth_handler.add_password(None, '23.106.159.52:3128', 'longer', 'longer')
#
# opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
# urllib2.install_opener(opener)
#
# url ='http://www.google.com'
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# print response.read()



import pandas as pd
import numpy as np

def change_date_to_month(date_str):
    return date_str[0:7]


data = pd.read_csv('D:/lzp.csv', header=0, dtype={'Date':np.str})
data.Date = data.Date.apply(change_date_to_month)
print data.Date
group = data.groupby('Date').sum()
print group





