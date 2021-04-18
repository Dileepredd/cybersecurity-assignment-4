# python DBSession = sessionmaker(bind=engine)  session = DBSession()
from database import tdb
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

@app.route('/register',methods = ["POST"])
def new_user():
    d = request.get_json(force=True)
    if 'username' not in d.keys():
        return Response('{"error":"username feild is missing"}',content_type="application/json",status=400)
    if 'password' not in d.keys():
        return Response('{"error":"password feild is missing"}',content_type="application/json",status=400)
    if tdb.register(d['username'],d['password']) == -1:
        return Response('{"error":"username already exist"}',content_type="application/json",status=400)
    return Response('{"status":"account is succesfully created"}',content_type="application/json",status=200)

@app.route('/token',methods = ["POST"])
def get_token():
    d = request.get_json(force=True)
    if 'username' not in d.keys():
        return Response('{"error":"username feild is missing"}',content_type="application/json",status=400)
    if 'password' not in d.keys():
        return Response('{"error":"password feild is missing"}',content_type="application/json",status=400)
    result = tdb.get_token(d['username'],d['password'])
    if result == -1:
        return Response('{"error":"username does not exist"}',content_type="application/json",status=400)
    else:
        return jsonify({"token":result})

@app.route('/newtoken',methods = ["POST"])
def generate_token():
    d = request.get_json(force=True)
    if 'username' not in d.keys():
        return Response('{"error":"username feild is missing"}',content_type="application/json",status=400)
    if 'password' not in d.keys():
        return Response('{"error":"password feild is missing"}',content_type="application/json",status=400)
    result = tdb.generate_token(d['username'],d['password'])
    if result == -1:
        return Response('{"error":"username does not exist"}',content_type="application/json",status=400)
    else:
        return jsonify({"token":result})

app.run()