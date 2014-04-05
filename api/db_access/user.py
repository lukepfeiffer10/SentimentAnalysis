import hashlib
from db import exec_proc
import story

# user

def assign_story(user_id):
    rc, rs = exec_proc("usp_story_assign", user_id)
    return rs if rc else rc

def select(user_id):
    rc, rs = exec_proc("usp_sel_user", user_id)
    return rs[0] if rc else False

def select_all():
    rc, rs = exec_proc("usp_sel_user_all")
    return {'users': rs} if rc else False

def select_page_info(user_id):
    rc, rs, = exec_proc("usp_sel_user_page_info", user_id)
    return rs[0] if rc else rc

# Return user_id, assigned story_id, and last_sentence_id on success
def insert(user_name, password, f_name, l_name):
    hash = hashlib.sha1(password).hexdigest()
    rc, rs = exec_proc("usp_ins_user", user_name, hash, f_name, l_name, True)
    return True if rc else False
    
# Return user_id, assigned_story_id on success, False otherwise
def authenticate(usr_name, password):
    hash = hashlib.sha1(password).hexdigest()
    rc, rs = exec_proc("usp_sel_user_auth", usr_name, hash)
    return rs[0]['user_id'] if rc else False

def delete(user_id):
    rc, rs = exec_proc("usp_del_user", user_id)
    return rc

def username_exists(user_name):
    rc, rs = exec_proc("usp_sel_user_by_name", user_name)
    return rc