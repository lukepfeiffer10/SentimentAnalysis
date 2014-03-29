from db import exec_proc



def insert_liwc_stem(stem):
    rc, rs = exec_proc("usp_ins_liwc_stem", stem)
    return rc