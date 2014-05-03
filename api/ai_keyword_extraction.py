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

def keyword_extraction(sentence_id, sentence):
    print "keyword_extraction"

    keywords = gen_keywords(sentence)   
    print "KEYWORDS: ", keywords
    
    #Identify if keywords are already in the db
    all_keywords = keyword_db.select_keywords()
    if all_keywords != None:
        keywords = [keyword for keyword in keywords if keyword not in all_keywords]
    if len(keywords) > 0:
        #Identify LIWC and GEN keywords from keywords
        liwc_keywords = gen_liwc_keywords(keywords)
        reg_keywords = [keyword for keyword in keywords if not (len([l_keyword for stem, l_keyword, id in liwc_keywords if l_keyword == keyword]) > 0)]
        for stem, keyword, id in liwc_keywords:
            keyword_db.insert_keyword(keyword, sentence_id, 0, id)
        for keyword in reg_keywords:
            keyword_db.insert_keyword(keyword, sentence_id, 0, None)
                
def gen_liwc_keywords(keywords):
    stem_lib = keyword_db.select_liwc_stems()
    if stem_lib != False:
        #Reformat Stem Lib
        stem_list = []
        for x in xrange(len(stem_lib)):
            temp_dict = dict(stem_lib[x])
            temp_list = [val for val in temp_dict.itervalues()]
            stem_list.append(temp_list)
        #Identify Stems, etc
        keywords = [[stem, keyword, id] for stem, id in stem_list for keyword in keywords if keyword.find(stem) == 0]
    else:
        keywords = []
    return keywords
                
def gen_keywords(sentence):
    words = word_tokenize(sentence)
    temp = []
    remove = ["(", ")", ".", ",", "[", "]", "''", "\\N", "\n", ":", "'", ";", "``", "&", "?", "!", "--", "p", "/p", "-", "style=", "quot", "text-align", "gt", "lt", "...", "t", "apos"]
    keywords = [word for word in words if word not in remove and word not in stopwords.words("english") and not contains_digit(word)]
    keywords = [str(word).replace("'", "") for word in keywords]
    keywords = [str(word).replace("/", "") for word in keywords]
    keywords = [str(word).replace("\\n", "") for word in keywords]
    keywords = [str(word).replace("\\N", "") for word in keywords]
    keywords = [str(word).replace("\n", "") for word in keywords]
    keywords = [str(word).replace("\\", "") for word in keywords]
    keywords = [str(word).replace("N", "") for word in keywords]
    return keywords
    
def contains_digit(word):
    _digits = re.compile('\d')
    return bool(_digits.search(word))    