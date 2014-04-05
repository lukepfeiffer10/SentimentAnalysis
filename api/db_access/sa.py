from db import exec_proc


def insert_liwc_stem(stem, tag_id):
    rc, rs = exec_proc("usp_ins_liwc_stem", stem, tag_id)
    return rc
    
def select_liwc_stems():
    rc, rs = exec_proc("usp_sel_liwc_stems")
    return rs if rc else False
    
def insert_keyword(keyword, sentence_id, negation_flg, liwc_tag_id = None):
    rc, rs = exec_proc("usp_ins_keyword", keyword, sentence_id, liwc_tag_id)
    return True if rc else False