from db import exec_proc, _pretty_print

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

def select_cluster(story_id):
    # This needs to be changed
    rc, rs = exec_proc("usp_sel_cluster", story_id)
    curr_cluster_id = 0
    arr = []
    sentences = []
    i = 0
    for v in rs:
        if i == 0:
            dict = {'sentiment': v['sentiment'].encode("utf-8"), 'length': v['length'], 'weight': v['weight'], 'type': v['type'].encode('utf-8')}
            sentences.append({'sentence_txt': v['sentence_txt']})
            curr_cluster_id = v['cluster_id']
        else:
            if v['cluster_id'] == curr_cluster_id:
                sentences.append({'sentence_txt': v['sentence_txt']})
            else:
                # finish dict and append to arr and reset
                dict['sentences'] = sentences
                arr.append(dict)
                dict = {'sentiment': v['sentiment'].encode("utf-8"), 'length': v['length'], 'weight': v['weight'], 'type': v['type'].encode('utf-8')}
                sentences = [{'sentence_txt': v['sentence_txt']}]
                curr_cluster_id = v['cluster_id']
    # last group
    
        i = 1
    return arr
    #print arr
            
            
    #return rs if rc else False

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