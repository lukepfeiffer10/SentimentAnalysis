delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_upd_keyword`(
IN keyword varchar(45),
IN tag_id INT,
IN stem_word varchar(45),
IN weight DOUBLE)
BEGIN

INSERT IGNORE INTO sa_stem (
stem_txt)
VALUES (
stem_word);

IF LAST_INSERT_ID() THEN
    SET @last_id = LAST_INSERT_ID();
ELSE
    SELECT sa_stem.id INTO @last_id
    FROM sa_stem
    WHERE sa_stem.stem_txt = stem_word;
END IF;

INSERT INTO sa_keyword (
keyword_txt,	
liwc_flg,
tag_id,
stem_id,
weight)
VALUES (
keyword,
0,
tag_id,
@last_id,
weight)
ON DUPLICATE KEY UPDATE
keyword_txt = keyword,
tag_id = tag_id,
weight = weight;

END$$

