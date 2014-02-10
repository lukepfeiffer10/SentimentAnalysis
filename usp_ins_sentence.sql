delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_ins_sentence`(
in story_id int(11),
IN sentence_txt varchar(250),
in seq_num int(11))
BEGIN
SET autocommit = 1;

INSERT INTO sentence(
story_id,
sentence_txt,
seq_num)
VALUES(
story_id,
sentence_txt,
seq_num);

END$$