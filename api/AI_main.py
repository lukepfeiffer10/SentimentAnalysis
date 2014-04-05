import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

import os
import csv
import shutil
import re

from db_access import story as story_db
from db_access import sentence as sentence_db

#84 = Userid, 13 = Userid
#13 = origi story
#21 = new origi story
#14 = my story

#ACTUAL FUNCTIONS USED IN THE WEBSITE
story_db_id = 21
def tokenize_story(story_db_id):
    print "tokenize_story"
    story = story_db.select_content(story_db_id)
    tokenized_story = sent_tokenize(story)
    for x in xrange(len(tokenized_story)):
        #print tokenized_story[x]
        sentence_id = sentence_db.insert(story_db_id, tokenized_story[x], x)
        keyword_extraction(tokenized_story[x])
        print sentence_id

def keyword_extraction(sentence):
    print "keyword_extraction"
    words = word_tokenize(sentence)
    english_stops = set(stopwords.words('english'))
    print words
    keywords = []
    
    from db_access import sa as stem_db
    stem_lib = stem_db.select_liwc_stems()
    print stem_lib
    """
    for word in words:
        if word not in english_stops:
            #stem_txt, tag_id
            #keywords.insert(0, word)
    print keywords"""
    
tokenize_story(story_db_id)
    
#TESTING
def main_testing():
    print "MAIN"
    imported_story = ""
    imported_story = import_story_test()
    tokenize_story_test(imported_story)
    #insert_story()
def import_story_test():
    print "import_story"
    story = story_db.select_content(21)
    print story
    print story_db.select_all()
    
    return story
def tokenize_story_test(imported_story):
    print "tokenize_story"
    #print imported_story
    tokenized_story = sent_tokenize(imported_story)
    for x in xrange(len(tokenized_story)):
        print tokenized_story[x]
        sentence_db.insert(21, tokenized_story[x], x)
def insert_story():
    print "insert_story"
    #story_db.insert(84, "I am a title", "I am a story. I do not include any special characters of any sort. That would be silly, and also not for me.")
    story_new = "Every morning, I take the city bus to school. The bus terminal near my apartment is pretty busy and it's not uncommon for me to get verbally harassed by men while I'm there waiting for my bus. Because of this, I was trying to mind my own business the other morning when a man approached me. I had my ipod in when I noticed him coming directly towards me. I avoided looking at him, hoping he would leave me alone, but no such luck. The next thing I knew, he was standing way too close to me and was talking to me. I turned my ipod off and asked him what he had said. He started asking me questions about my ipod and then asked me how old I was. I told him I was 20 and he looked me up and down and said \"Some pretty for only 20...\" I started to text my friend hoping that if I ignored him he'd move away, but he didn't. Each time I stepped away from him, he'd step closer again. I was starting to feel threatened so I walked away to the other side of the terminal, pretending to look at the bus schedule. The man followed behind me without hesitation. As I was looking at the schedule he started asking me what bus I was taking, I ignored him and walked away again, back where I had come from. He continued following me. I walked into an area with a larger group of people and he still followed me. He was still standing too close, and was looking me up and down my body. I was so creeped out and my heart was beating so fast. He had this look in his eye that told me there was something not right with him. I wanted to tell him to get away from me, but at the time I was so scared. I was worried that if I told him to leave he may react badly, I didn't want to escalate the situation. After what felt like a lifetime, but was really a few minutes, his bus came and he left. Shortly after, a friend of mine arrived and we got on the bus to go to school. On the bus, I told her what had happened and we got to comparing stories about the various times that men have harassed us and about how generally messed up our society is. During this conversation, the man sitting in front of us kept peeking around and looking at us. It was clear that he was eavesdropping. When he got off the bus, he walked by our window and stared at us, then licked his lips and winked as we drove away. We were completely taken aback. After everything he had probably just heard us say, he had the nerve to do that!I thought about that morning for the rest of the day. I was angry at myself for giving someone else the power to make me feel scared. I was angry at myself for not standing up when I should have. I am constantly being harassed by men, and ignoring it obviously is not working for me. I'm done with keeping my head down and my mouth shut. From now on I WILL hollaback!"
    story_db.insert(84, "This is an actual story", story_new)


#main_testing()
