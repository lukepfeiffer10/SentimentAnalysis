from db import exec_proc

# sentence

# Start sequence at 0 to be consistent
def insert(story_id, sentence_txt, seq_num):
    rc, rs = exec_proc("usp_ins_sentence", story_id, sentence_txt, seq_num)
    return True if rc else False

def select_next(user_id, num_before = 0, num_after = 0):
    rc, rs = exec_proc("usp_sel_sentence", user_id, num_before, num_after)
    return {'sentences': rs} if rc else False

# Call this only if isLegit() returns true
def tag(user_id, sentence_id, tag_id):
    rc, rs = exec_proc("usp_tag_sentence", user_id, sentence_id, tag_id)
    return True if rc else False

# Validate a sentence to be tagged.
def validate(user_id, sentence_id, tag_id):
    rc, rs = exec_proc("usp_sentence_validate", user_id, sentence_id, tag_id)
    return rs[0]['legit']