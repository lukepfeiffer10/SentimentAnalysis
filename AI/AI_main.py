import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

import os
import csv
import shutil
import re

import story as story_db
import sentence as sentence_db

#84 = Userid, 13 = Userid
#13 = origi story
#14 = my story

def main():
    print "MAIN"
    imported_story = ""
    imported_story = import_story()
    tokenize_story(imported_story)
    #insert_story()

def import_story():
    print "import_story"
    story = story_db.select_content(13)
    print story
    print story_db.select_all()
    
    return story

def tokenize_story(imported_story):
    print "tokenize_story"
    #print imported_story
    tokenized_story = sent_tokenize(imported_story)
    for x in xrange(len(tokenized_story)):
        print tokenized_story[x]
        sentence_db.insert(13, tokenized_story[x], x)

def insert_story():
    print "insert_story"
    story_db.insert(84, "I am a title", "I am a story. I do not include any special characters of any sort. That would be silly, and also not for me.")

main()
