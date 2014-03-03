from db import exec_proc



def select_all():
    rc, rs = exec_proc("usp_sel_tag_all")
    return rs[0] if rc else False