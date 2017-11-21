# Setting Up Flask
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
server = Flask(__name__)

# Importing Other Modules
import requests

# Importing Custom Modules
from app import main

# Serving HTML Pages/Templates

f = open('templates/data.txt', 'r+')

posts = eval('''[
	('sample name', 'sample body', 'sample time')
]''')

@server.route('/')
def home():
	return render_template('home.html', posts=posts)

@server.route('/store', methods = ['POST', 'GET'])
def store():
	if request.method == 'POST':
		f.write(str(posts)) #the text in the file should resemble a columnar list
		return home() #takes it back to a blank webpage
	f.close()

@server.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404