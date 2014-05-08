delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_user_auth`(
IN user_name varchar(45),
IN password varchar(100))
BEGIN
SELECT user.id as user_id
FROM user
WHERE user.user_name = user_name AND user.password = password;
END$$

