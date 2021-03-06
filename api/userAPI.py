#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for, session
from flask.views import MethodView
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from db_access import sentence, user

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)
parser.add_argument('firstName', type=str)
parser.add_argument('lastName', type=str)

class UserAPI(Resource):

    def __init__(self):
        super(UserAPI, self).__init__()
        
    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        first_name = args['firstName']
        last_name = args['lastName']
        
        return user.insert(username, password, first_name, last_name)
            

    def put(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        u_id  = user.authenticate(username, password)
        if (u_id):
            session['u_id'] = u_id
            return True
        else:
            return False, 401

    def delete(self):
        session.pop('u_id', None)