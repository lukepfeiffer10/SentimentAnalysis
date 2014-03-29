from db import exec_proc



def insert_liwc_stem(stem):
    rc, rs = exec_proc("usp_ins_liwc_stem", stem)
    return rc
    
def select_liwc_stems():
    rc, rs = exec_proc("usp_sel_liwc_stems")
    return rs if rc else False