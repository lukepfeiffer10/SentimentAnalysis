delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_story_assign`(
IN user_id INT)
BEGIN
SET @assigned_story = 0;

SELECT story.id INTO @assigned_story
FROM story
LEFT OUTER JOIN sentence
    ON story.id = sentence.story_id
LEFT OUTER JOIN tag_for_sentence AS ts
    ON ts.sentence_id = sentence.id
WHERE story.last_sentence_id  IS NOT NULL 
  AND story.user_id != user_id 
  AND NOT EXISTS (
	  SELECT * FROM tag_for_sentence as t
	  WHERE t.user_id = user_id AND sentence.story_id = story.id)
GROUP BY story.story_title
ORDER BY COUNT(ts.tag_id) ASC
LIMIT 1;

UPDATE user_app_data
SET assigned_story = @assigned_story;

SELECT @assigned_story;

END$$