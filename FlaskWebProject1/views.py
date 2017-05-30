"""
Routes and views for the flask application.
"""

from FlaskWebProject1 import app
from flask import jsonify
import json

events_path = './FlaskWebProject1/sources/events.json'
itens_path = './FlaskWebProject1/sources/itens.json'
events = []
itens = []


def update_events():
    # Get Events
    f = open(events_path, 'r')
    events_file = f.read()
    events_j = json.loads(events_file)
    for event in events_j:
        events.append(event)
    f.close()


def update_itens():
    # Get Itens
    f = open(itens_path, 'r')
    itens_file = f.read()
    itens_j = json.loads(itens_file)
    for it in itens_j:
        itens.append(it)
    f.close()


@app.route('/')
@app.route('/home')
def home():
    return 'Hello World'


@app.route('/api/herdeiros/events/all')
def get_all_events():
    return jsonify(events)


@app.route('/api/herdeiros/events/all_2')
def get_all_events_2():
    return str(len(events))


@app.route('/api/herdeiros/itens/all')
def get_all_itens():
    return jsonify(itens)


@app.route('/api/herdeiros/item/create/<name>/<description>')
def create_item(name, description):
    item = {}
    item['name'] = name
    item['description'] = description
    itens.append(item)
    itens_file = json.dumps(itens, indent=2)
    f = open(itens_path, 'w+')
    f.write(str(itens_file))
    f.close()
    return 'Item created with success!'


@app.route('/api/herdeiros/event/create/<name>/<date>')
def create_event(name, date):
    evento = {}
    evento['name'] = name
    evento['date'] = date
    events.append(evento)
    events_file = json.dumps(events, indent=2)
    f = open(events_path, 'w+')
    f.write(str(events_file))
    f.close()
    return 'Event created with success!'
