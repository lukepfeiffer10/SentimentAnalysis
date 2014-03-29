from db import exec_proc

# sentence

# Start sequence at 0
def insert(story_id, sentence_txt, seq_num):
    rc, rs = exec_proc("usp_ins_sentence", story_id, sentence_txt, seq_num)
    return rs[0]['sentence_id'] if rc else False
    
def select_current_group(user_id):
    rc, rs = exec_proc("usp_sel_sentence_group", user_id)
    return {'sentences': rs} if rc else False

def select_sentence_tags():
    rc, rs = exec_proc("usp_sel_sentence_tags")
    return rs if rc else False

def tag(user_id, sentence_id, tag_id):
    rc, rs = exec_proc("usp_tag_sentence", user_id, sentence_id, tag_id)
    return rs if rc else False

# Validate a sentence to be tagged.
def validate(user_id, sentence_id, tag_id):
    rc, rs = exec_proc("usp_sentence_validate", user_id, sentence_id, tag_id)
    return rs[0]['legit']