# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 11:54:23 2015

@author: andylane
"""

import django
import urllib
import urllib2
import json

path_to_image = "landscape.jpg"
desired_url = "http://www.youtube.com"

##################
#### Get a token
url = 'https://www.livepaperapi.com/auth/v1/token'

params = {
  'Authorization': 'Basic dW40bzFna2VidXdyMDF1ajE0a3Qzd2p5eTYwMGVqaTg6dGo1SmxPMkZvVU01VTd1NTQ3Ujl0UnlLc3k2bDk2cTI=',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
}

data = "grant_type=client_credentials&scope=default"
req = urllib2.Request(url, data, params)
f = urllib2.urlopen(req)
response = f.read()
# f.close()
# print f

response = json.loads(response)

################
#### Make a Payoff
url = 'https://www.livepaperapi.com/api/v1/payoffs'

params = {
  'Authorization': str('Bearer ' + response['accessToken']),
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}


data = json.dumps({'payoff': {"URL":desired_url, "name":"your youtube video"}})
# '["foo", {"payoff": ["baz", null, 1.0, 2]}]'
# data = ""
# print params
# print data
payoff_request = urllib2.Request(url, data, params)
payoff_response = urllib2.urlopen(payoff_request).read()
payoff_response = json.loads(payoff_response)
# print(payoff_response)
payoff_ID = (payoff_response["payoff"]["id"])

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
# print(trigger_response)

#YOU MIGHT NEED THIS!
trigger_URL = (trigger_response["trigger"]["link"][0]["href"])
trigger_ID = (trigger_response["trigger"]["id"])

################
#### Upload a file

url = 'https://storage.livepaperapi.com/objects/v1/files'

params = {
  'Authorization': str('Bearer ' + response['accessToken']),
  'Content-Type': 'image/jpeg',
  'Accept': 'application/json',
}

data = open(path_to_image, "rb").read()

# print data

image_post = urllib2.Request(url, data, params)
image_response = urllib2.urlopen(image_post).info().headers
#image_response=json.loads(image_response)
image_URL = image_response[-4][10:-2]
#image_response = json.loads(image_response)
print(image_response)

################
#### Get that file? If you want, not necessary?

url = image_url
#query = urllib.urlencode({'width': '100'})
print(response['accessToken'])

#url = url+"?"+query
params = {	
  'Authorization': str('Bearer ' + response['accessToken']),
  'Accept': 'image/jpeg',
}

image_get_request = urllib2.Request(url)
image_get_request.headers = params
image_get_item = urllib2.urlopen(image_get_request)
f = open('00000001.jpg','wb')
f.write(image_get_item.read())
f.close()


################
#### Make a link between a trigger and a payoff

url = 'https://www.livepaperapi.com/api/v1/links'

params = {
  'Authorization': str('Bearer ' + response['accessToken']),
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

data = json.dumps({'link': {"payoffId":payoff_ID, "name":"picture2video", "triggerId":trigger_ID}})
trigger_request = urllib2.Request(url, data, params)
trigger_response = urllib2.urlopen(trigger_request).read()
trigger_response = json.loads(trigger_response)


################
#### Download the watermarked file
url = trigger_URL
query = urllib.urlencode({'imageURL': image_URL, 'resolution':'75', 'strength':'10'})
#print(response['accessToken'])

url = url+"?"+query

params = {
  'Authorization': str('Bearer ' + response['accessToken']),
  'Content-Type': 'application/json',
  'Accept': 'image/jpg',
}

wmimage_get_request = urllib2.Request(url)
wmimage_get_request.headers = params
wmimage_get_item = urllib2.urlopen(wmimage_get_request)
f = open('wm00000001.jpg','wb')
f.write(wmimage_get_item.read())
f.close()

