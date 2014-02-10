delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_del_story`(
IN user_id INT,
IN story_id INT)
BEGIN
set autocommit = 1;
DELETE FROM story
WHERE user_id = user_id AND id = story_id;
END$$