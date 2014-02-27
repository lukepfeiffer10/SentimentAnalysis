#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for, session
from flask.views import MethodView
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from db_access import sentence, user



class SentencesAPI(Resource):

    def __init__(self):
        super(SentencesAPI, self).__init__()
        
    def get(self):
        sentences = sentence.select_next(session['u_id'],100,100)
        return sentences