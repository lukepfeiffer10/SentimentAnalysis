delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_ins_user`(
IN user_name varchar(45),
in password varchar(100),
IN first_name varchar(45),
IN last_name  varchar(45))
BEGIN
SET autocommit = 1;

INSERT INTO user(
user_name,
password)
VALUES(
user_name,
password);

INSERT INTO person(
user_id,
first_name,
last_name)
VALUES(
LAST_INSERT_ID(),
first_name,
last_name);

SELECT id
FROM user
WHERE user.id = LAST_INSERT_ID();

END$$





