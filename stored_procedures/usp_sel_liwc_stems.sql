delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_liwc_stems`()
BEGIN
SET autocommit = 1;

SELECT stem_txt, tag_id
FROM sa_liwc_stem;
END$$