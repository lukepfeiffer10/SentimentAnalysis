#Cluster Code to Be Altered

import MySQLdb

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet

import os
import csv
import shutil
import re
import random
import sys

import numpy as np
from numpy import loadtxt

#Connect to DB
db = MySQLdb.connect(host="174.74.50.196", # your host, usually localhost
                     user="remote", # your username
                      passwd="mountaindew", # your password
                      db="sentiment_analysis") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

def cluster_story(story_id):
    print "story_id: ", story_id 
    cluster_data = generate_cluster_data(story_id)
    insert_cluster_data(story_id, cluster_data)
    
def insert_cluster_data(story_id, cluster_data):
    #cluster_id = gen_cluster_id()
    #print "CLUSTER_ID: ", cluster_id
    for cluster in cluster_data:
        cluster_length = gen_cluster_length(cluster)
        cluster_type = "average"
        sql = "INSERT INTO `sa_cluster`(`sentiment`, `length`, `weight`, `type`) VALUES ('%s', %s, %s, '%s' );"
        cur.execute(sql % (str(cluster[2]), str(cluster_length), str(cluster[3]), cluster_type))
        cluster_id = cur.lastrowid
        insert_into_sent_cluster(cluster_id, cluster)
    try:
        db.commit()
    except MySQLdb.Error, e:
        print "query failed<br/>"
        print e
        
def insert_into_sent_cluster(cluster_id, cluster):
    for sent in cluster[1]:
        sql = "INSERT INTO `sa_sentence_cluster`(`sentence_id`, `cluster_id`) VALUES ( %s, %s );"
        cur.execute(sql % (str(sent), str(cluster_id)))
        print "SQL for SENT CLUSTER: ", sql
 
def gen_cluster_length(cluster_data):
    print "gen_cluster_length"
    words = 0
    for x in xrange(len(cluster_data[1])):
        sql = "SELECT sentence_txt FROM sentence WHERE id = %s"
        cur.execute(sql  % (str(cluster_data[1][x])))
        sent_txt = cur.fetchone()[0]
        sent_len = len(word_tokenize(sent_txt))
        words += sent_len
    return words

def gen_cluster_id():
    sql = "select max(id) from sa_cluster"
    cur.execute(sql)
    max = (cur.fetchone()[0]) + 1
    return max

def generate_cluster_data(story_id):
    tokenized_story = retrieve_sent_information(story_id)
    story_sentiment_info = gen_sentence_sentiment(tokenized_story)
    cluster_data = cluster_algorithm(story_sentiment_info)
    return cluster_data
    
def cluster_algorithm(story_sentences):
    cluster_temp = []
    temp = []
    prev_sentiment = -2
    for x in xrange(len(story_sentences)):
        curr_sentiment = story_sentences[x][4][0]
        #start first cluster
        if len(temp) == 0:
            prev_sentiment = curr_sentiment
            temp.append(story_sentences[x])
        #start new cluster (!first)
        elif prev_sentiment != curr_sentiment and len(temp) > 0:
            #Handle Previous Cluster
            sentence_assoc_data = [row[0] for row in temp]
            temp_np = np.array([row[4][1] for row in temp])
            cluster_avg = float(float(sum(temp_np))/float(len(temp)))
            cluster_temp.append([story_sentences[x][1], sentence_assoc_data, prev_sentiment, cluster_avg])
            #Start New Temp Val
            temp = []
            prev_sentiment = curr_sentiment
            temp.append(story_sentences[x])
        #add to current cluster
        elif prev_sentiment == curr_sentiment:
            #print "SAME SENTIMENT"
            temp.append(story_sentences[x])
      
        if (x == len(story_sentences)-1):
            #print "LAST CLUST"
            sentence_assoc_data = [row[0] for row in temp]
            temp_np = np.array([row[4][1] for row in temp])
            cluster_avg = float(float(sum(temp_np))/float(len(temp)))
            cluster_temp.append([story_sentences[x][1], sentence_assoc_data, prev_sentiment, cluster_avg])
    return cluster_temp
    
def gen_sentence_sentiment(tokenized_story):
    import ai_module
    classifier = ai_module.train_classifier()
    temp = [[row1, row2, row3, sent, ai_module.classify(sent, classifier)] for row1, row2, row3, sent in tokenized_story]
    return temp

def retrieve_sent_information(story_id):
    sql = "select * from sentence where story_id = %s"
    sql += " group by seq_num"
    cur.execute(sql % (str(story_id)))
    temp = [[row[0], row[1], row[2], row[3]] for row in cur.fetchall()]
    return temp
