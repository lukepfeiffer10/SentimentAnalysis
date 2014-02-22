from db import *

# story

def insert(user_id, story_title, story_content):
    status, rc, rs = exec_proc("usp_ins_story", user_id, story_title, story_content)
    return True if status and rc else False

# Call this once after inserting all sentences for a particular story
def insert_complete(story_id):
    status, rc, rs = exec_proc("usp_ins_story_complete", story_id)
    return True if status else False

def select_all():
    status, rc, rs = exec_proc("usp_sel_story_all")
    return {'stories': rs} if status else False

def select_all_by_author(user_id):
    status, rc, rs = exec_proc("usp_sel_story_all_by_author", user_id)
    return {'stories': rs} if status else False

def select_least_tagged():
    dummy = 0
    status, rc, rs = exec_proc("usp_sel_story_least_tagged", dummy)
    return rs if status else False

def select_content(story_id):
    status, rc, rs = exec_proc("usp_sel_story_content", story_id)
    return rs[0]['story_content']

def delete(user_id, story_id):
    status, rc, rs = exec_proc("usp_del_story", user_id, story_id)
    return True if status else False
