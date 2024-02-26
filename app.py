import configparser
from flask import Flask, request, render_template, Response, url_for

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
        project = ''
        if fname.startswith('zeeschuimer'):
            project = Load().load_zeeschuimer(fname)
        else:
            project = Load().load(fname)
        return url_for('project.html', id=project)
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
        return render_template('timeline.html')
  