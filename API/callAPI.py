# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 11:54:23 2015

@author: andylane
"""

import django
import urllib
import urllib2
import json

# Get a token
url = 'https://www.livepaperapi.com/auth/v1/token'

params = {
  'Authorization': 'Basic dW40bzFna2VidXdyMDF1ajE0a3Qzd2p5eTYwMGVqaTg6dGo1SmxPMkZvVU01VTd1NTQ3Ujl0UnlLc3k2bDk2cTI=',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  # 'Body':'grant_type=client_credentials&scope=default',
  # 'grant_type': 'REQUIRED'
}

data = "grant_type=client_credentials&scope=default"
req = urllib2.Request(url, data, params)
f = urllib2.urlopen(req)
response = f.read()
# f.close()
# print f

response = json.loads(response)
# print(response['accessToken'])

################
#### Make a Payoff
url = 'https://www.livepaperapi.com/api/v1/payoffs'

params = {
  'Authorization': str('Bearer ' + response['accessToken']),
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}


data = json.dumps({'payoff': {"URL":"http://www.youtube.com", "name":"your youtube video"}})
# '["foo", {"payoff": ["baz", null, 1.0, 2]}]'
# data = ""
# print params
# print data
payoff_request = urllib2.Request(url, data, params)
payoff_response = urllib2.urlopen(payoff_request).read()
payoff_response = json.loads(payoff_response)
# print(payoff_response)

'''
For each uploaded image:
- Make a Trigger ID
- Make a Payoff ID
- Link the Trigger and Payoff IDs
- Upload an image associated with the Trigger

'''


################
#### Make a Trigger

url = 'https://www.livepaperapi.com/api/v1/triggers'

params = {
  'Authorization': str('Bearer ' + response['accessToken']),
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

data = json.dumps({'trigger': {"URL":"http://www.youtube.com", "name":"a picture of me on the beach", "type":"watermark"}})
trigger_request = urllib2.Request(url, data, params)
trigger_response = urllib2.urlopen(trigger_request).read()
trigger_response = json.loads(trigger_response)
print(trigger_response)

print(trigger_response["trigger"]["link"][0]["href"])