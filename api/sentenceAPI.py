#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for, session
from flask.views import MethodView
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from db_access import sentence, user

parser = reqparse.RequestParser()
parser.add_argument('sentence_id', type=int)
parser.add_argument('tag_id', type=int)

class SentencesAPI(Resource):

    def __init__(self):
        super(SentencesAPI, self).__init__()
        
    def get(self):
        sentences = sentence.select_next(session['u_id'],100,100)
        return sentences
        
    def put(self):
        args = parser.parse_args()
        sentence_id = args['sentence_id']
        tag_id = args['tag_id']
        return sentence.tag(session['u_id'], sentence_id, tag_id)     