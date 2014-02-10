delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_story_all`()
BEGIN
SELECT id, story_title
FROM story as s
order by story_title DESC;
END$$

