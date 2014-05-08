delimiter $$
# If we want users to switch stories inbetween tagging, this will need to be changed
CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_ins_story_complete`(
IN story_id INT)
BEGIN
SET autocommit = 1;
UPDATE story
SET sentence_count = (
    SELECT COUNT(1)
    FROM sentence
    WHERE sentence.story_id = story.id)
WHERE story.id = story_id;
END$$