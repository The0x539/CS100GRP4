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

#f = open('templates/data.txt', 'r+')

posts = []
items = []
tup = ()

#@server.route('/getall') #collects all data from file and stores in a list called posts
def getall():
	with open('sarbani.txt') as file:
		 for line in file:
		 	items.append(eval(line))
		 posts = list(set(items))#checks list for duplicate items, removes them if present
		 
@server.route('/')
def home():
	getall()#gets all the data and displays on homepage
	return render_template('home.html', posts=posts)
	       
        
@server.route('/store', methods = ['POST', 'GET'])
def store():#stores data from form
	if request.method == 'POST':
		date = str(request.form['date'])
		body = str(request.form['body'])
		time = str(request.form['time'])
		tup = date, body, time
	with open('templates/data.txt','a+') as file:
		file.write((str(tup))+"\n") #the text in the file should resemble a columnar list
		return home() #takes it back to a blank webpage
	

@server.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404