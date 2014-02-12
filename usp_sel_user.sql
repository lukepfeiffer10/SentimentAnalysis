delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_user`(
IN user_id INT)
BEGIN
SELECT user.id, user.user_name, person.first_name, person.last_name
FROM user
LEFT OUTER JOIN person 
	on user.id = person.user_id
WHERE user.id = user_id;
END$$