# Setting Up Flask
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import redirect

server = Flask(__name__)

# Importing Other Modules
import requests

from app import main

# Serving HTML Pages/Templates

#collects all data from file and stores in a list
def getall():
	with open('templates/data.txt') as file:
		items = []
		for line in file:
			items.append(eval(line))
		return list(set(items)) #checks list for duplicate items, removes them if present

@server.route('/', methods = ['GET'])
def home():
	return render_template('home.html', posts=getall())

@server.route('/invalid', methods = ['GET'])
def invalid():
	return render_template('home.html',posts=getall(),invalid=True)

@server.route('/store', methods = ['POST'])
def store():#stores data from form
	def form(name):
		return str(request.form[name])
	date = form('date')
	body = form('body')
	time = form('time')
	location = form('location')
	if date == '' or body == '' or time == '' or location == '':
		return redirect('/invalid',code=302)
	tup = (date, body, time, location)
	with open('templates/data.txt','a+') as file:
		file.write((str(tup))+"\n") #the text in the file should resemble a columnar list
	return redirect('/',code=302) #takes it back to a blank webpage

@server.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404