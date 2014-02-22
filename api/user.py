import hashlib
from db import exec_proc
import story

# user

def select(user_id):
    status, rc, rs = exec_proc("usp_sel_user", user_id)
    return rs[0] if rc else False

def select_all():
    status, rc, rs = exec_proc("usp_sel_user_all")
    return {'users': rs} if rc else False

# Return user_id on success
def insert(user_name, password, f_name, l_name, auto_assign_story = False):
    if not select_by_name(user_name): # if user_name is not already taken
        hash = hashlib.sha1(password).hexdigest()
        status, rc, rs = exec_proc("usp_ins_user", user_name, hash, f_name, l_name, auto_assign_story)
        return (True, rs[0]['user_id'], rs[0]['last_sentence_id']) if rc else (False, 1)
    else:
        return False, 2

# Return user_id on success
def authenticate(usr_name, password):
    hash = hashlib.sha1(password).hexdigest()
    status, rc, rs = exec_proc("usp_sel_user_auth", usr_name, hash)
    return (True, rs[0]['id']) if rc else (False, 1)

def delete(user_id):
    status, rc, rs = exec_proc("usp_del_user", user_id)
    return True if rc else False

def select_by_name(user_name):
    status, rc, rs = exec_proc("usp_sel_user_by_name", user_name)
    return rs[0] if rc else False

