delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_ins_user`(
IN user_name varchar(45),
in password varchar(100),
IN first_name varchar(45),
IN last_name  varchar(45),
IN auto_assign_story INT)
BEGIN
declare assigned_story int default 0;
SET autocommit = 1;

INSERT INTO user(
user_name,
password)
VALUES(
user_name,
password);

SET @user_id = LAST_INSERT_ID();

INSERT INTO person(
user_id,
first_name,
last_name)
VALUES(
@user_id,
first_name,
last_name);

call usp_sel_story_to_assign(@user_id, assigned_story);
-- SET assigned_story_id = 13;

INSERT INTO user_app_data(
user_id,
assigned_story_id)
VALUES(
@user_id,
assigned_story);

END$$

