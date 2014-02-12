from db import *

# sentence

# Start sequence at 0 to be consistant
def insert(story_id, sentence_txt, seq_num):
    rc, rs = exec_proc("usp_ins_sentence", story_id, sentence_txt, seq_num)
    return True if rc else False

# start_index is the sequence number of the sentence
def select(story_id, start_index, count):
    rc, rs = exec_proc("usp_sel_sentence", story_id, start_index, count)
    return {'sentences': rs} if rc else False

# Will override previous tag if user has already tagged sentence
def tag(user_id, sentence_id, tag_id):
    rc, rs = exec_proc("usp_tag_sentence", user_id, sentence_id, tag_id)
    return True if rc else False
