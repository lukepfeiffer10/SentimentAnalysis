delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_sentence_tags`()
BEGIN
SET autocommit = 1;
SELECT sentence.id, sentence.sentence_txt, ts.tag_id
FROM sentence
inner join tag_for_sentence ts
    on ts.sentence_id = sentence.id;
END$$