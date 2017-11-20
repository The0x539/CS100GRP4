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

@server.route('/hello')
def hello():
    return 'Hello World'

# Serving HTML Pages/Templates

@server.route('/')
def home():
    return render_template('index.html', name='Visitor')
    
@server.route('/name/<name>')
def name(name=None):
    return render_template('index.html', name=name)

f = open('templates/data.txt', 'r+')

posts = eval('''[
    ('sample name', 'sample body', 'sample time')
]''')

@server.route('/foo')
def foo():
    return render_template('foo.html', posts=posts)

@server.route('/store', methods = ['POST', 'GET'])
def store():
    if request.method == 'POST':
        
        f.write(str(posts)) #the text in the file should resemble a columnar list
        return render_template('foo.html',posts=posts)#takes it back to a blank webpage
    f.close()

@server.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Responding to Requests with Data

@server.route('/reflect/<name>')
def reflect(name=None):
    r = {'name': name}
    return jsonify(r)
    
@server.route('/weather')
def weather():
    w = main.get_weather()
    return jsonify(w)
    
@server.route('/location_image/<search>')
def location_image(search):
    geo_url = "https://maps.googleapis.com/maps/api/geocode/json"
    geo_query = {
        "address": search
    }
    geo_res = requests.request("GET", geo_url, params=geo_query);
    geo_data = geo_res.json();
    loc = geo_data['results'][0]['geometry']['location'];
    url = "https://maps.googleapis.com/maps/api/streetview"
    querystring = {
        "size": "600x600",
        "location": str(loc['lat']) + "," + str(loc['lng']),
        "heading": "90",
        "pitch": "0"
    }
    response = requests.request("GET", url, params=querystring)
    return response.url;