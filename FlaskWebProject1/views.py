"""
Routes and views for the flask application.
"""

from FlaskWebProject1 import app
from flask import jsonify
import json

events_path = './FlaskWebProject1/sources/events.json'
itens_path = './FlaskWebProject1/sources/itens.json'

f = open(events_path, 'r')
events_file = []
events_file = f.read()
events = json.loads(events_file)
f.close()
f = open(itens_path, 'r')
itens_file = []
itens_file = f.read()
itens = json.loads(itens_file)
f.close()



@app.route('/')
@app.route('/home')
def home():
    return 'Hello World'

@app.route('/teste')
def teste():
    return 'teste working'


@app.route('/api/herdeiros/eventos/all')
def get_all_events():
    return jsonify(events)


@app.route('/api/herdeiros/itens/all')
def get_all_itens():
    return jsonify(itens)


@app.route('/api/herdeiros/item/create/<name>/<description>')
def create_events(name, description):
    item = {}
    item['name'] = name
    item['description'] = description
    item_j = json.dumps(item)
    itens.append(item_j)
    f = open(itens_path, 'w+')
    f.write(itens)
    f.close()
    return 'Event created with success!'


@app.route('/api/herdeiros/eventos/create/<name>/<date>')
def create_events(name, date):
    evento = {}
    evento['name'] = name
    evento['date'] = date
    evento_j = json.dumps(evento)
    events.append(evento_j)
    f = open(events_path, 'w+')
    f.write(events)
    f.close()
    return 'Event created with success!'