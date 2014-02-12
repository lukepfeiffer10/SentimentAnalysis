from db import *
import story

# user

def select(user_id):
    rc, rs = exec_proc("usp_sel_user", user_id)
    return rs[0] if rc else False

def select_all():
    rc, rs = exec_proc("usp_sel_user_all")
    return {'users': rs} if rc else False

# Return user_id on success, false on failure
# Assume false means user_name taken
# Setting last parameter to True will assign to the user the least tagged story
def insert(user_name, password, f_name, l_name, auto_assign_story = False):
    if not select_by_name(user_name): # if user_name is not already taken
        hash = hashlib.sha1(password).hexdigest()
        rc, rs = exec_proc("usp_ins_user", user_name, hash, f_name, l_name, auto_assign_story)
        return rs[0]['id'] if rc else False
    else:
        return False;

# Return user_id on success, false on failure
def authenticate(usr_name, password):
    hash = hashlib.sha1(password).hexdigest()
    rc, rs = exec_proc("usp_sel_user_auth", usr_name, hash)
    return rs[0]['id'] if rc else False

def delete(user_id):
    rc, rs = exec_proc("usp_del_user", user_id)
    return True if rc else False

def select_by_name(user_name):
    rc, rs = exec_proc("usp_sel_user_by_name", user_name)
    return rs[0] if rc else False
