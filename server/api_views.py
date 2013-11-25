from server import app
from flask import jsonify,g,request
from server.api import *

@app.route('/users', methods = ['GET','PUT'])
def users():
    if request.method == 'GET':
        return jsonify(get_users())
    elif request.method == 'PUT':
        if not request.json:
            abort(400)
        return jsonify(add_user())
