delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_del_user`(
IN user_id INT)
BEGIN
set autocommit = 1;
DELETE FROM user
WHERE id = user_id;
END$$


