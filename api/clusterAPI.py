#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for, session
from flask.views import MethodView
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from db_access import story
import AI_main as AI

class ClusterAPI(Resource):

    def __init__(self):
        super(ClusterAPI,self).__init__()

    def get(self):
        return story.select_cluster(session['u_id'])