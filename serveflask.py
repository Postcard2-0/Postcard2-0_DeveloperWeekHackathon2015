from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
import sys
from werkzeug import secure_filename

"""
Created on Sat Feb  7 11:54:23 2015

@author: andylane
"""

import urllib
import urllib2
import json
import datetime
path_to_input_image = "landscape.jpg"
uniqueID = "user0001"
desired_url = "http://www.youtube.com"

'''
For each uploaded image:
- Get an authentication token
- Make a Trigger ID
- Make a Payoff ID
- Link the Trigger and Payoff IDs
- Upload an image associated with the Trigger

'''

############## ANDY


##################
#### Get a token
def get_access_token():
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
	response = json.loads(response)
	return(response['accessToken'])

################
#### Make a Payoff
def define_target_URL(access_token, desired_url):
	url = 'https://www.livepaperapi.com/api/v1/payoffs'

	params = {
	  'Authorization': str('Bearer ' + access_token),
	  'Content-Type': 'application/json',
	  'Accept': 'application/json',
	}

	data = json.dumps({'payoff': {"URL":desired_url, "name":"your youtube video"}})
	payoff_request = urllib2.Request(url, data, params)
	payoff_response = urllib2.urlopen(payoff_request).read()
	payoff_response = json.loads(payoff_response)
	payoff_ID = (payoff_response["payoff"]["id"])
	return payoff_ID

################
#### Make a Trigger

def set_up_trigger(access_token, uniqueID):
	'''
	This sets up the data to be encoded in an image to be retrieved later with get_watermarked_image().
	
	INPUT: uniqueID(str): Should be a unique name for the trigger encoded in the image.
	'''
	url = 'https://www.livepaperapi.com/api/v1/triggers'

	params = {
	  'Authorization': str('Bearer ' + access_token),
	  'Content-Type': 'application/json',
	  'Accept': 'application/json',
	}
	startDate = str(datetime.datetime.now().isoformat()[0:-3] + "+0800")
	endDate = datetime.datetime.now() + datetime.timedelta(days = 365)
	endDate = str(endDate.isoformat()[0:-3] + "+0800")

	data = json.dumps({'trigger': {"name": uniqueID, "type":"watermark", "startDate": startDate, "endDate": endDate}})
	trigger_request = urllib2.Request(url, data, params)
	trigger_response = urllib2.urlopen(trigger_request).read()
	trigger_response = json.loads(trigger_response)

	#These are referred to when making the link and when watermarking an image
	trigger_URL = (trigger_response["trigger"]["link"][0]["href"])
	trigger_ID = (trigger_response["trigger"]["id"])
	return(trigger_URL, trigger_ID)

################
#### Upload a file
def send_file_to_HP(access_token, path_to_input_image):
	url = 'https://storage.livepaperapi.com/objects/v1/files'

	params = {
	  'Authorization': str('Bearer ' + access_token),
	  'Content-Type': 'image/jpeg',
	  'Accept': 'application/json',
	}

	data = open(path_to_input_image, "rb").read()
	image_post = urllib2.Request(url, data, params)
	image_response = urllib2.urlopen(image_post).info().headers
	image_URL = image_response[-4][10:-2]
	return(image_URL)

################
#### Get that file? If you want, not necessary?
def download_original_file_from_HP(access_token, image_URL, directoryprefix= ""):
	url = image_URL
	# Can uncomment these two lines to specify a size to download
	#query = urllib.urlencode({'width': '100'})
	#url = url+"?"+query

	params = {	
	  'Authorization': str('Bearer ' + access_token),
	  'Accept': 'image/jpeg',
	}

	image_get_request = urllib2.Request(url)
	image_get_request.headers = params
	image_get_item = urllib2.urlopen(image_get_request)
	f = open(directoryprefix+"original_"+path_to_input_image,'wb')
	f.write(image_get_item.read())
	f.close()

################
#### Make a link between a trigger and a payoff
def link_trigger_to_URL(access_token, trigger_ID, payoff_ID):
	url = 'https://www.livepaperapi.com/api/v1/links'

	params = {
	  'Authorization': str('Bearer ' + access_token),
	  'Content-Type': 'application/json',
	  'Accept': 'application/json',
	}

	data = json.dumps({'link': {"payoffId":payoff_ID, "name":"picture2video", "triggerId":trigger_ID}})
	link_request = urllib2.Request(url, data, params)
	urllib2.urlopen(link_request)

################
#### Download the watermarked file
def download_watermarked_image(access_token, image_URL, trigger_URL, directoryprefix= ""):
	url = trigger_URL
	query = urllib.urlencode({'access_token': access_token, 'imageURL': image_URL, 'resolution':'75', 'strength':'10'})
	url = url+"?"+query

	params = {
	  'Authorization': str('Bearer ' + access_token),
	  'Accept': 'image/jpg',
	}

	wmimage_get_request = urllib2.Request(url)
	wmimage_get_request.headers = params
	wmimage_get_item = urllib2.urlopen(wmimage_get_request)
	f = open(str(directoryprefix+"watermarked_" + path_to_input_image),'wb')
	f.write(wmimage_get_item.read())
	f.close()
	return wmimage_get_item


class image_video_pair:
	'''
	Contains a watermarked image from a piece of input
	'''
	def __init__(self, path_to_input_image, path_to_input_video, desired_url):
		self.picture = path_to_input_image
		self.video = path_to_input_video
		access_token = get_access_token()
		payoff_ID = define_target_URL(access_token, desired_url)
		trigger_URL, trigger_ID = set_up_trigger(access_token, uniqueID)
		image_URL = send_file_to_HP(access_token, path_to_input_image)
		link_trigger_to_URL(access_token, trigger_ID, payoff_ID)
		watermarked = download_watermarked_image(access_token, image_URL, trigger_URL, directoryprefix= "")
		self.watermarked = watermarked

########### ANDY


reload(sys)
sys.setdefaultencoding('utf-8')


# Initialize flask applicaiton
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALOWED_EXTENSIONS'] = set(['jpg','avi','tif','mov'])

t = 0

# Open default URL 
@app.route('/')
def test():
	print("Hello world!")
	return render_template('index.html')

@app.route('/submit/', methods=['POST'])
def submit():
	print("Submitting photo...")
	sender_name = request.form['SenderName']
	memo = request.form['SenderMemo']
	file = request.files['photo']
	filename = secure_filename(file.filename)
	filename = file.filename
	# file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	print(filename)
	stamped = image_video_pair('/Users/ucsf/Documents/Accelerate_Hackathon/Post2/Cats.jpg','video','http://www.youtube.com')

	
	if(t == 1):
		sender_memo = request.form['SenderMemo']
		rec_name = request.form['RecName']
		rec_street = request.form['Street']
		rec_st_nr = reuqest.form['StreetNr']
		rec_city = request.form['City']
		rec_country = request.form['Country']

	print(sender_name)
	return render_template('submit.html', SenderName = sender_name, SenderMemo = memo, watermarked = stamped.watermarked)


# run the app
if 	__name__ == '__main__':
	app.run()
