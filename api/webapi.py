#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from sentenceAPI import SentencesAPI
 
app = Flask(__name__, static_url_path = "")
api = Api(app)
        
api.add_resource(SentencesAPI, '/api/sentences/next', endpoint= 'sentences')
    
if __name__ == '__main__':
    app.run(debug = True, port=5000)