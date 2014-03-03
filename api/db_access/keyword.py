from db import exec_proc



def insert_liwc(keyword, tag_id, stem):
    rc, rs = exec_proc("usp_ins_liwc_keyword", keyword, tag_id, stem)
    return rc
    
    
