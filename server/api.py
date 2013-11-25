from Crypto.PublicKey import RSA
from flask import g, request, abort
import datetime

def get_users():
    cur = g.db.execute('select id, name, date, public_key from users')
    
    users = [{'id':row[0], 'name':row[1], 'join_date':row[2], 'key':row[3]} for row in cur.fetchall()]
    return {'users':users}

def add_user():
    if not request.json:
        abort(400)

    data = request.get_json()

    if 'name' not in data:
        abort(400)
    if 'key' not in data:
        abort(400)
    if 'registration_id' not in data:
        abort(400)
    
    # Try and verify the key
    try:
        key = RSA.importKey(data['key'])
    except ValueError:
        abort(400)

    join_date = datetime.datetime.now()

    insert_sql = "insert into users values (NULL,?,?,?,?)"

    cur = g.db.execute(insert_sql,[data['name'],join_date,data['registration_id'],str(key.exportKey())])
    g.db.commit()

    return {'id':cur.lastrowid}
