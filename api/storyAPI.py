#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for, session
from flask.views import MethodView
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from db_access import story
import AI_main as AI

parser = reqparse.RequestParser()
parser.add_argument('content', type=str)
parser.add_argument('title', type=str)

class StoryAPI(Resource):

    def __init__(self):
        super(StoryAPI,self).__init__()

    def post(self):
        args = parser.parse_args()
        storyText = args['content']
        title = args['title']
        storyID = story.insert(session['u_id'],title, storyText)
        AI.tokenize_story(storyID)
        story.insert_complete(storyID)
        return {'id':storyID}
        