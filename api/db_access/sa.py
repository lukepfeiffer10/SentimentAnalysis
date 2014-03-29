from db import exec_proc


def insert_liwc_stem(stem, tag_id):
    rc, rs = exec_proc("usp_ins_liwc_stem", stem, tag_id)
    return rc
    
def select_liwc_stems():
    rc, rs = exec_proc("usp_sel_liwc_stems")
    return rs if rc else False