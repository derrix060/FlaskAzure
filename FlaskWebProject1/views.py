"""
Routes and views for the flask application.
"""

from FlaskWebProject1 import app

events_path = './FlaskWebProject1/sources/events.json'
itens_path = './FlaskWebProject1/sources/itens.json'

f = open(events_path, 'r')
events = []
events = f.read()
f.close()
f = open(itens_path, 'r')
itens = []
itens = f.read()
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
    return events


@app.route('/api/herdeiros/itens/all')
def get_all_itens():
    return jsonify(itens)


@app.route('/create_events')
def create_events():
    eventos = []
    evento = {}
    evento['name'] = 'teste name'
    evento['date'] = "2017-06-05 17:00:00"
    eventos.append(evento)
    eventos.append(evento)
    eventos.append(evento)
    rtn = jsonify(eventos)
    f = open(events_path, 'w+')
    f.write(rtn)
    f.close()
    return rtn