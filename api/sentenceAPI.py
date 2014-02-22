#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.views import MethodView
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
import user 
import story
import sentence

class SentencesAPI(Resource):

    def __init__(self):
        super(SentencesAPI, self).__init__()
        
    def get(self):
        x,y = sentence.select_next(84,100,100)
        return y