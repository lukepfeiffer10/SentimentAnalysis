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


def main():
    print "main"
    #import_liwc_data()
    insert_liwc_keyword(None, 2, "low*")

def insert_liwc_keyword(liwc_keyword, liwc_sentiment, liwc_stem):
    #Note: positive = 1, negative = 2, neutral = 3
    
    sys.path.append("C:\\Users\\A\\Documents\\GitHub\\SentimentAnalysis\\api")
    from db_access import keyword_sa as keyword_db
    #print "insert_liwc_keyword"
    keyword_db.insert_liwc(liwc_keyword, liwc_sentiment, liwc_stem)
    print "ADDING: " + str(liwc_keyword) + " " + str(liwc_sentiment) + " " + str(liwc_stem)


def import_liwc_data():
    print "import_liwc_data"
    paths = [pos_liwc_data_path, neg_liwc_data_path]
    for path in paths:
         with open(path, 'rb') as csvfile:
            treader = csv.reader(csvfile)
            for row in treader:
                if len(row[0]) != 0:
                    print row
                    for word in row:
                        letters = []
                        letters = word
                        """
                        if '*'not in letters and word != "":
                            print letters, "AST"
                            if path == "pos_liwc_data_path":
                                insert_liwc_keyword(word, 1, word)
                            else:
                                insert_liwc_keyword(word, 2, word)"""
                        if '*' in letters:
                            #WordNetLemmatizer.lemmatize
                            print word
                        
                        
                            
main()
