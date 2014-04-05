import sys
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

import os
import csv
import shutil
import re

pos_liwc_data_path = "C:\\Users\\A\\Documents\\GitHub\\SentimentAnalysis\\AI\\LIWC_UPLOAD\\pos_liwc_dataset.csv"
neg_liwc_data_path = "C:\\Users\\A\\Documents\\GitHub\\SentimentAnalysis\\AI\\LIWC_UPLOAD\\neg_liwc_dataset.csv"

def liwc_stem_upload():
    data = []
    import_liwc_data(data)
    #print data
    insert_liwc_stems(data)

def insert_liwc_stems(data):
    sys.path.append("C:\\Users\\A\\Documents\\GitHub\\SentimentAnalysis\\api")

    from db_access import sa as keyword_db

    for stem in data:
        keyword_db.insert_liwc_stem(stem[0], stem[1])
        print "ADDING: " + str(stem)

def import_liwc_data(data):
    print "import_liwc_data"
    paths = [pos_liwc_data_path, neg_liwc_data_path]
    for path in paths:
         with open(path, 'rb') as csvfile:
            treader = csv.reader(csvfile)
            for row in treader:
                if len(row[0]) != 0:
                    #print row
                    for word in row:
                        letters = []
                        letters = word
                        if '*' in letters:
                            m_word = word.translate(None, '*')
                            if path == pos_liwc_data_path:
                                data.append([m_word, 1])
                            else:
                                data.append([m_word, 3])

liwc_stem_upload()
