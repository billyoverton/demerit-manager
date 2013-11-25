from flask import Flask, g, request
import sqlite3
app = Flask(__name__)
app.config.from_object('server.default_settings')
app.config.from_envvar('DEMERIT_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


import server.views
import server.api_views
