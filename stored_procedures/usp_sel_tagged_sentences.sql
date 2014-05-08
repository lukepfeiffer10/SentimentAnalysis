delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_tagged_sentences`()
BEGIN

SELECT sentence.sentence_txt, ts.tag_id
FROM tag_for_sentence ts
inner join sentence
    on ts.sentence_id = sentence.id;

END$$