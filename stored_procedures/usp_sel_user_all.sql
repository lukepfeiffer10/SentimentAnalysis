delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_user_all`()
BEGIN
SELECT id, user_name 
FROM user;
END$$

