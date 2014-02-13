delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_user_auth`(
IN user_name varchar(45),
IN password varchar(100))
BEGIN
SELECT id
FROM user as u
WHERE u.user_name = user_name AND u.password = password;
END$$

