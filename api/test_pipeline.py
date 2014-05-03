#This File Begins the Pipeline for AI System Testing

import AI_main as ai_main

def main():
    print "START PIPELINE TEST"
    #story_db_id = 47
    story_db_id = 55
    ai_main.tokenize_story(story_db_id)

main()
