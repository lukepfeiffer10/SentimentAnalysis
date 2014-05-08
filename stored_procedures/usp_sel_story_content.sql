delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_story_content`(
IN story_id INT)
BEGIN

select story_content
from story
where story.id = story_id;

END$$

