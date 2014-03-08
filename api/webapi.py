#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for, session, render_template
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from sentenceAPI import SentencesAPI
from userAPI import UserLoginAPI
 
app = Flask(__name__, static_url_path = "/static", template_folder = "../")
api = Api(app)

api.add_resource(SentencesAPI, '/api/sentences/next', endpoint= 'sentences')
api.add_resource(UserLoginAPI, '/api/user/login', endpoint= 'login')

@app.route('/')
def renderIndex():
    return render_template('index.html')
    
@app.route('/login')
def renderLogin():
    return render_template('login.html')

app.secret_key = '\xd9\xa4\xf9hQ\x82`k9Y\xca7,0\x05gmj\xee\x16\x98Y\x8b\x98'


if __name__ == '__main__':
    app.run(debug = True, port=5000)