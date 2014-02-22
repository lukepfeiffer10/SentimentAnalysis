from db import exec_proc

# sentence

# Start sequence at 0 to be consistant
def insert(story_id, sentence_txt, seq_num):
    status, rc, rs = exec_proc("usp_ins_sentence", story_id, sentence_txt, seq_num)
    return True if rc else False

def select_next(user_id, num_before = 0, num_after = 0):
    status, rc, rs = exec_proc("usp_sel_sentence", user_id, num_before, num_after)
    if status:
        return True, {'sentences': rs}
    else:
        return False, 1

# Returns sentence with seq_num = last_seq_num++
def tag(user_id, sentence_id, tag_id, last_seq_num):
        status, rc, rs = exec_proc("usp_tag_sentence", user_id, sentence_id, tag_id, last_seq_num)
        if status:
            return True, rs
        else:
            return False, 2

# Validate a sentence to be tagged. 
def isLegit(user_id, story_id, sentence_id):
        status, rc, rs = exec_proc("usp_is_sentence_legit", user_id, story_id, sentence_id)
        return rs
