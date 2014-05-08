delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_tag_all`()
BEGIN
SELECT *
FROM tag;
END$$