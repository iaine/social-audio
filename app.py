import configparser
#from db import DB as d
from flask import Flask, request, render_template, jsonify, Response

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('social.ini')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/load', methods=['GET', 'POST'])
def load():
    if request.method == "GET":
        return render_template('load.html')
    elif request.method == "POST":
        return render_template('load.html')
    else:
        return render_template('load.html')