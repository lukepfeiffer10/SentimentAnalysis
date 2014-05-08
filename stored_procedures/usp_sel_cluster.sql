delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_cluster`(
IN story_id INT)
BEGIN
select c.id as cluster_id, c.sentiment, c.length, c.weight, c.type, sentence.sentence_txt
from sa_cluster c
inner join sa_sentence_cluster sc
    on c.id = sc.cluster_id
inner join sentence
    on sc.sentence_id = sentence.id
where sentence.story_id = story_id
order by c.id;

END$$