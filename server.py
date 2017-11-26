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

#@server.route('/getall') #collects all data from file and stores in a list called posts
def getall():
	with open('templates/data.txt') as file:
		items = []
		for line in file:
			items.append(eval(line))
		return list(set(items)) #checks list for duplicate items, removes them if present

@server.route('/', methods = ['GET'])
def home(invalid=False):
	return render_template('home.html', posts=getall(), invalid=invalid)

@server.route('/', methods = ['POST'])
def store():#stores data from form
	def form(name):
		return str(request.form[name])
	date = form('date')
	body = form('body')
	time = form('time')
	if date == '' or body == '' or time == '':
		return home(invalid=True)
	tup = (date, body, time)
	with open('templates/data.txt','a+') as file:
		file.write((str(tup))+"\n") #the text in the file should resemble a columnar list
	return home() #takes it back to a blank webpage

@server.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404