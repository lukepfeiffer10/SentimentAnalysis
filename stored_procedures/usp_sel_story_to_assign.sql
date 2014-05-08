delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_story_to_assign`(
IN user_id INT,
OUT storyid INT)
BEGIN
SET storyid = 0;
SELECT story_id INTO storyid
FROM story
LEFT OUTER JOIN sentence
    ON story.id = sentence.story_id
LEFT OUTER JOIN tag_for_sentence AS ts
    ON ts.sentence_id = sentence.id
WHERE story.sentence_count  IS NOT NULL
      AND story.user_id != user_id
      AND NOT EXISTS (
	      SELECT * FROM tag_for_sentence as t
	      WHERE t.user_id = user_id AND sentence.story_id = story_id)
GROUP BY story.story_title
ORDER BY COUNT(ts.tag_id) ASC
LIMIT 1;

END$$