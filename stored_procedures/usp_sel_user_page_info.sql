delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_user_page_info`(
IN user_id INT)
BEGIN
SELECT first_name, last_name, total_tag_count, story_title
FROM person
INNER JOIN user_app_data as ud
    ON ud.user_id = person.user_id
INNER JOIN story
    ON story.id = ud.assigned_story_id
WHERE person.user_id = user_id;
END$$