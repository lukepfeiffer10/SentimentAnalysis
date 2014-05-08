delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_ins_liwc_stem`(
IN stem varchar(45),
IN tag_id INT)
BEGIN
SET autocommit = 1;

INSERT INTO sa_liwc_stem(stem_txt, tag_id) VALUES (stem, tag_id);
END$$