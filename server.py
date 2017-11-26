# Setting Up Flask
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request


server = Flask(__name__)

# Importing Other Modules
import requests

from app import main

# Serving HTML Pages/Templates

f = open('templates/data.txt', 'r+')

posts = []
tup = ()
@server.route('/')
def home():
	return render_template('home.html', posts=posts)
@server.route('/getall') #adds to file
def getall():
	with open('templates/data.txt','r+') as file:
    		items = file.read().split("\n")
    		for i in posts:
        		if i is '(' or i is ')':
        			pass
        		else: pass
        
        
@server.route('/store', methods = ['POST', 'GET'])
def store():#stores data from form
	if request.method == 'POST':
		date = str(request.form['date'])
		body = str(request.form['body'])
		time = str(request.form['time'])
		tup = date, body, time
	with open('templates/data.txt','r+') as file:
		file.write((str(tup))+"\n") #the text in the file should resemble a columnar list
		return home() #takes it back to a blank webpage
	

@server.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404