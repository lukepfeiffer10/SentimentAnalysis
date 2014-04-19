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

story_db_id = 21
def tokenize_story(story_db_id):
    print "tokenize_story"

    #import story
    story = story_db.select_content(story_db_id)
    #tokenize story
    tokenized_story = sent_tokenize(story)
    #import liwc stem library
    from db_access import sa as stem_db
    stem_lib = stem_db.select_liwc_stems()

    test_keyword = 'asdf'
    #1 = Negation
    #0 = Normal
    #insert_keyword(test_keyword, 1, )

    #loop through tokenized story and insert into sentence db, extract keywords, compare to liwc_lib
    for x in xrange(len(tokenized_story)):
        #insert sentence into sentence db
        sentence_id = sentence_db.insert(story_db_id, tokenized_story[x], x)
        #extract keywords from sentence
        #keyword_extraction(sentence_id, tokenized_story[x], stem_lib)
        #print sentence_id

    #Determine Sentence Sentiment Using NLTK methodology functions
    #Develop the Sentence Structure

def keyword_extraction(sentence_id, sentence, stem_lib):
    from db_access import sa as stem_db
    
        
    words = word_tokenize(sentence)
    english_stops = set(stopwords.words('english'))
    
    keywords = []
    #Generate Keywords List
    for word in words:
        if word not in english_stops:
            #stem_txt, tag_id
            keywords.append(word)
    #print keywords
    #Insert Keywords into DB

    stem_dict = dict(stem_lib)

    if 'keen' in stem_dict.values():
        print "KEEN FOUND"

    """
    for stem_txt, tag_id in stem_lib.iteritems():
        if stem_txt == "keen":
            print "KEEN FOUND!"
            
    for keyword in keywords:
        for x in xrange(len(stem_lib)):
            print stem_lib[x]
            if stem_lib[x].find(keyword):
                print "FOUND"
                print stem_lib[x]
                print keyword
            #if keyword in stem_lib:
                #print "MATCH: ", keyword
                #insert_keyword"""


#tokenize_story(story_db_id)
