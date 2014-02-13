delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_story_all_by_author`(
IN user_id VARCHAR(45))
BEGIN
SELECT id, story_title
FROM story as s
WHERE s.user_id = user_id
order by story_title DESC;
END$$
