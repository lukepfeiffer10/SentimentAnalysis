delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_ins_keyword`(
IN keyword varchar(45),
IN sentence_id INT,
IN negation_flg INT,
IN liwc_tag_id INT)
BEGIN
SET autocommit = 1;

insert into sa_keyword (
keyword_txt,
liwc_tag_id)
values (
keyword,
liwc_tag_id)
on duplicate key update id = LAST_INSERT_ID();

insert into sa_keyword_sentence (
sentence_id,
keyword_id,
negation_flg)
values (
sentence_id,
LAST_INSERT_ID(),
negation_flg);

END$$