from db import *

def insert(user_id, story_title, story_content):
    rc, rs = exec_proc("usp_ins_story", user_id, story_title, story_content)
    return rs[0]['story_id']

# Call this once after inserting all sentences for a particular story
def insert_complete(story_id):
    rc, rs = exec_proc("usp_ins_story_complete", story_id)
    return rc

def select_all():
    rc, rs = exec_proc("usp_sel_story_all")
    return {'stories': rs} if rc else False

def select_all_by_author(user_id):
    rc, rs = exec_proc("usp_sel_story_all_by_author", user_id)
    return {'stories': rs} if rc else False

def select_content(story_id):
    rc, rs = exec_proc("usp_sel_story_content", story_id)
    return rs[0]['story_content']

def delete(user_id, story_id):
    rc, rs = exec_proc("usp_del_story", user_id, story_id)
    return rc

def title_exits(user_id, story_title):
    return 0