from flask import Flask
from flask import render_template
from flask import request


# Initialize flask applicaiton
app = Flask(__name__)


# Open default URL to select destination 
@app.route('/')
def form():
	return render_template('index.html')



# run the app
if 	__name__ == '__main__':
	app.run()
