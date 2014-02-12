from db import *

# story

def insert(user_id, story_title, story_content):
    rc, rs = exec_proc("usp_ins_story", user_id, story_title, story_content)
    return True if rc else False

def select_all():
    rc, rs = exec_proc("usp_sel_story_all")
    return {'stories': rs} if rc else False

def select_all_by_author(user_id):
    rc, rs = exec_proc("usp_sel_story_all_by_author", user_id)
    return {'stories': rs} if rc else False

def select_least_tagged():
    dummy = 0
    rc, rs = exec_proc("usp_sel_story_least_tagged", dummy)
    return rs if rc else False


def delete(user_id, story_id):
    rc, rs = exec_proc("usp_del_story", user_id, story_id)
    return True if rc else False


