import nltk
import collections

# Needed for filtering out stopwords
from nltk.corpus import stopwords

# NLTK's significant bigram library
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

# Test Stories
testStories = [ ("There was once an ugly barnacle. He was so ugly, that everyone died. The end.", "neg"),
("\tOnce upon a time, a princess was trapped in a castle in a far away land. This castle was guarded day and night by a dragon that kills anyone that dares set foot on the castle grounds. A knight in shining armor came to challenge the dragon and to save the princess.\n\tBased on sheer courage alone, the dragon was slain by the knight. The princess was overjoyed to be saved by the knight, instantly falling in love with him. The knight reveals that he is a prince, allowing them to marry and live happily ever after.", "pos") ]

def bag_of_words(words):
    return dict([(word, True) for word in words])

def bag_of_words_not_in_set(words, badwords):
    return bag_of_words(set(words) - set(badwords))

def bag_of_non_stopwords(words, stopfile='english'):
    badwords = stopwords.words(stopfile)
    return bag_of_words_not_in_set(words, badwords)
    
def bag_of_bigrams_words(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    return bag_of_words(words + bigrams)
    
def label_feats_from_corpus(corp, feature_detector=bag_of_words):
    label_feats = collections.defaultdict(list)
    for label in corp.categories():
        for fileid in corp.fileids(categories=[label]):
            feats = feature_detector(corp.words(fileids=[fileid]))
            label_feats[label].append(feats)
    return label_feats
    
def split_label_feats(lfeats, split=0.75):
    train_feats = []
    test_feats = []
    for label, feats in lfeats.iteritems():
        cutoff = int(len(feats) * split)
        train_feats.extend([(feat, label) for feat in feats[:cutoff]])
        test_feats.extend([(feat, label) for feat in feats[cutoff:]])
    return train_feats, test_feats
        
