#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for, session
from flask.views import MethodView
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from db_access import sentence, user

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)

class UserLoginAPI(Resource):

    def __init__(self):
        super(UserLoginAPI, self).__init__()
        
    # Test to simulate what the post function would do
    # if successful 
    def get(self):
        session['u_id'] = 90
        session['story_id'] = 13
        session['last_sentence_id'] = 50
        session.permanent = False
        return True
        
    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        u_id, story_id, last_sentence_id = user.authenticate(username, password)
        if (u_id):
            session['u_id'] = u_id
            session['story_id'] = story_id
            session['last_sentence_id'] = last_sentence_id
            return True
        else:
            return False