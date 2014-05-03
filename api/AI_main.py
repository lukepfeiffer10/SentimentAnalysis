#This File Contains the AI pipelining where the data goes from
# 1: The API Calls tokenize_story
#    --> The Story is Tokenized
#    --> The Tokenized Stories are imported into the database
#    --> keyword_extraction is called
#    --> cluster_story is called

#import nltk libraries
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
#import python libraries
import os
import csv
import shutil
import re
#import db libraries
from db_access import story as story_db
from db_access import sentence as sentence_db

from db_access import sa as keyword_db

import ai_keyword_extraction as ke_file

import ai_clustering as clustering

def tokenize_story(story_db_id):
    print "tokenize_story"
    #import story
    story = story_db.select_content(story_db_id)
    #tokenize story
    unicode_story = story.encode("utf-8")
    tokenized_story = sent_tokenize(unicode_story)
    
    #1 = Negation, 0 = Normal, insert_keyword(test_keyword, 1, )
    for x in xrange(len(tokenized_story)):
        print "sentence_text: ", tokenized_story[x]
        sentence_id = sentence_db.insert(story_db_id, tokenized_story[x], x)
        #ke_file.keyword_extraction(sentence_id, tokenized_story[x])    
        #generate_sentence_sentiment(sentence_id, tokenized_story[x])
        #print sentence_id        
    clustering.cluster_story(story_db_id)

def generate_sentence_sentiment(sentence_id, sentence):
    print "generate_sentence_sentiment"