delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_ins_story`(
IN user_id int(11),
in story_title varchar(100),
IN story_content longtext)
BEGIN
SET autocommit = 1;

INSERT INTO story(
user_id,
story_title,
story_content)
VALUES(
user_id,
story_title,
story_content);

select LAST_INSERT_ID() as story_id;

END$$