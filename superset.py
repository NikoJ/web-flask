#!/usr/bin/python3

#/slicemodelview/api/read
#/superset/slice_query/2
#/superset/slice_json/2


import sys
import requests
import urllib
from bs4 import BeautifulSoup
import os

#test
os_host = os.environ.get('SS_HOST')
os_test_name = os.environ.get('SS_TEST_USER')
os_test_pass = os.environ.get('SS_TEST_PASS')

ss_host = f"http://{os_host}:9088"
ss_name = os_test_name
ss_pass = os_test_pass

# set up session for auth
s = requests.Session()
login_form = s.post(ss_host+"/login")

# get Cross-Site Request Forgery protection token
soup = BeautifulSoup(login_form.text, 'html.parser')
csrf_token = soup.find('input',{'id':'csrf_token'})['value']
print(csrf_token)

# login the given session
s.post(ss_host + '/login/',data=dict(username=ss_name, password=ss_pass,csrf_token=csrf_token))

# form the request
encoded = urllib.quote(sys.argv[1])
print(encoded)

# execute the request
res=s.get(ss_host + encoded)
print(res)
print(res.text)