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
    print(d)
    print(d.keys())
    if tdb.register(d['username'],d['password']) == -1:
        return Response('{"error":"username already exist"}',content_type="application/json",status=400)
    return jsonify(d)

@app.route('/token',methods = ["GET"])
def get_token():
    return "hello"

@app.route('/newtoken',methods = ["GET"])
def generate_token():
    return "hello"

app.run()