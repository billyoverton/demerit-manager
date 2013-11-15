from flask import Flask
app = Flask(__name__)
app.config.from_object('server.default_settings')
import server.views
