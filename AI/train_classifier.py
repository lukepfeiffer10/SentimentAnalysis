# python script to train a classifier based on corpus and write to file pickle dump 'nb_classifier'

import pickle
from nltk.classify import NaiveBayesClassifier
from featx import *

# to be replaced with our own corpus
from nltk.corpus import movie_reviews
corpus = movie_reviews

# load classifier
# nb_classifier = pickle.load(open('nb_classifier', 'rb'))

lfeats = label_feats_from_corpus(corpus)
train_feats, test_feats = split_label_feats(lfeats)
nb_classifier = NaiveBayesClassifier.train(train_feats)

# dump to file (WARNING: File will be overwritten)
pickle.dump(nb_classifier, open('nb_classifier', 'wb'))