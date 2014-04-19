import nltk
import collections
import pickle
import sys

# Needed for filtering out stopwords
from nltk.corpus import stopwords

# NLTK's significant bigram library
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

from nltk import word_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import CategorizedPlaintextCorpusReader

sys.path.append('..\\')
from tag_enum import *

# Test Stories
testStories = [ ("There was once an ugly barnacle. He was so ugly, that everyone died. The end.", "neg"),
("\tOnce upon a time, a princess was trapped in a castle in a far away land. This castle was guarded day and night by a dragon that kills anyone that dares set foot on the castle grounds. A knight in shining armor came to challenge the dragon and to save the princess.\n\tBased on sheer courage alone, the dragon was slain by the knight. The princess was overjoyed to be saved by the knight, instantly falling in love with him. The knight reveals that he is a prince, allowing them to marry and live happily ever after.", "pos") ]

def bag_of_words(words):
    """Constructor for bag of words. Reference: NLTK Cookbook Ch. 7"""
    return dict([(word, True) for word in words])

def bag_of_words_not_in_set(words, badwords):
    """Constructor for bag of words not in set. Reference: NLTK Cookbook Ch. 7"""
    return bag_of_words(set(words) - set(badwords))

def bag_of_non_stopwords(words, stopfile='english'):
    """Constructor for bag of non-stopwords. Reference: NLTK Cookbook Ch. 7"""
    badwords = stopwords.words(stopfile)
    return bag_of_words_not_in_set(words, badwords)
    
def bag_of_bigrams_words(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
    """Constructor for bag of bigrams words. Reference: NLTK Cookbook Ch. 7"""
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    return bag_of_words(words + bigrams)
    
def label_feats_from_corpus(corp, feature_detector=bag_of_words):
    """Labels feats from corpus. Reference: NLTK Cookbook Ch. 7"""
    label_feats = collections.defaultdict(list)
    for label in corp.categories():
        for fileid in corp.fileids(categories=[label]):
            feats = feature_detector(corp.words(fileids=[fileid]))
            label_feats[label].append(feats)
    return label_feats
    
def split_label_feats(lfeats, split=0.75):
    """Splits label feats. Reference: NLTK Cookbook Ch. 7"""
    train_feats = []
    test_feats = []
    for label, feats in lfeats.iteritems():
        cutoff = int(len(feats) * split)
        train_feats.extend([(feat, label) for feat in feats[:cutoff]])
        test_feats.extend([(feat, label) for feat in feats[cutoff:]])
    return train_feats, test_feats
    
def train_classifier(corpus=CategorizedPlaintextCorpusReader('./corpus/', r'.+\.txt', cat_pattern=r'(.+)\.txt')):
    """Trains a classifier and stores it in file 'nb_classifier'
    
    Parameters:
        corpus - The corpus system used to train classifier
                 Default: corpus system stored in ./corpus/
        
    Returns:
        The classifier stored in 'nb_classifier'
    """
    lfeats = label_feats_from_corpus(corpus)
    train_feats, test_feats = split_label_feats(lfeats, 1)
    nb_classifier = NaiveBayesClassifier.train(train_feats)
    pickle.dump(nb_classifier, open('nb_classifier', 'wb'))
    return nb_classifier
    
def classify(sent, classifier=None):
    """Classifies a sentence based on the classifier passed.
    
    Parameters:
        sent       - Sentence to classify
        classifier - NaiveBayesClassifier object used to classify
                     Default: object loaded from 'nb_classifier' file
        
    Returns:
        Category that was classified
        Weight of returned category
    """
    if classifier == None:
        try:
            classifier=pickle.load(open('nb_classifier', 'rb'))
        except IOError as e:
            print("Error: nb_classifier file not found")
            return
        except:
            print("Unexpected Error")
            return
    cat = classifier.classify(bag_of_words(word_tokenize(sent)))
    weight = classifier.prob_classify(bag_of_words(word_tokenize(sent))).prob(cat)
    return cat, weight
    
def update_sentences(sentences, classifier=None):
    """Updates the sentences of the database with pos or neg tags. If the sentence is tagged, an update will be made to the corpus with the sentence. If untagged, the current classifier will tag it and update the corpus with the sentence.
    
    Parameters:
        sentences   - list of dictionaries using the following format:
                      [{"sentence_text": "I am happy.", "tag_id": 1}, ...]
                      Tag number is represented by tag_enum.py
        classifier  - classifier for automatic tagging.
                      If none given, loads classifier stored in 'nb_classifier'
    
    Returns:
        Updated sentences
    """
    if classifier == None:
        try:
            classifier=pickle.load(open('nb_classifier', 'rb'))
        except IOError as e:
            print("Error: nb_classifier file not found")
            return
        except:
            print("Unexpected Error")
            return
    
    corNeg = None
    corPos = None
    corNeu = None
    try:
        corNeg = open('corpus\\neg.txt', 'ab')
        corPos = open('corpus\\pos.txt', 'ab')
        corNeu = open('corpus\\neu.txt', 'ab')
    except:
        print("Error: Loading Corpus")
    for sent_d in sentences:
        sent = sent_d["sentence_text"]
        tagged = sent_d["tag_id"]
        if tagged == None or tagged == '':
            # tag does not exist
            cat, weight = classify(sent, classifier)
            # tagged = cat
        # update corpus
        if tagged == tag.neg:
            corNeg.write('\n'+sent)
        if tagged == tag.pos:
            corPos.write('\n'+sent)
        if tagged == tag.neu:
            corNeu.write('\n'+sent)
    corNeg.close()
    corPos.close()
    corNeu.close()
    return sentences
