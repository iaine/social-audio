import configparser
from flask import Flask, request, render_template, jsonify, Response

from database import database as db
from load import Load

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
        fname = request.form["media"]

        if fname.startswith('zeeschuimer'):
            Load().load_zeeschuimer(fname)
        else:
            Load().load(fname)
        return render_template('load.html')
    else:
        return render_template('load.html')
    
@app.route('/project/<id>')
def project(id):
    if id is None:
        projects = []
        #get proejcts
        return render_template('project.html', projects = projects)
    else:
        #get data by proect id
        return render_template('project.html', projects = [])
    
@app.route('/project/<id>/timeline')
def project(id):
    if id is None:
        projects = []
        #get proejcts
        return render_template('project.html', projects = projects)
    else:
        #get data by proect id
        projects = db.get_data_by_id(id)
        return render_template('timeline.html', projects = [])
  