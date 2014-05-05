#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for, session, render_template
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from sentenceAPI import SentencesAPI, SentencesListAPI
from userAPI import UserAPI
from storyAPI import StoryAPI
 
app = Flask(__name__, static_url_path = "/static", template_folder = "../")
api = Api(app)

api.add_resource(SentencesListAPI, '/api/sentences', endpoint= 'sentences')
api.add_resource(SentencesAPI, '/api/sentences/<int:id>', endpoint= 'sentence')
api.add_resource(UserAPI, '/api/user', endpoint= 'user')
api.add_resource(StoryAPI, '/api/story', endpoint='story')

@app.route('/')
def renderIndex():
    if session.has_key('u_id'):
        return render_template('index.html')
    else:
        return renderLogin()

@app.route('/login')
def renderLogin():
    return render_template('login.html')
    
@app.route('/about')
def renderAbout():
    return render_template('about.html')

@app.route('/about_researcher')
def renderAboutResearcher():
    return render_template('about_researcher.html')
    
@app.route('/upload')
def renderStoryUpload():
    return render_template('upload.html')

app.secret_key = '\xd9\xa4\xf9hQ\x82`k9Y\xca7,0\x05gmj\xee\x16\x98Y\x8b\x98'


if __name__ == '__main__':
    app.run(debug = True, port=5000)
