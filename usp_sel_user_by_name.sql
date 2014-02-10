delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_user_by_name`(
IN user_name varchar(45))
BEGIN
SELECT user.id, user.user_name, person.first_name, person.last_name
FROM user
LEFT OUTER JOIN person 
	on user.id = person.user_id
WHERE user.user_name = user_name;
END$$