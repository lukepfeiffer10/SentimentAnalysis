delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_sentence`(
IN story_id int(11),
IN start_index int(11),
IN count int(11))
BEGIN
# user? security?
SELECT id, sentence_txt, seq_num
FROM sentence
WHERE sentence.story_id = story_id AND 
      seq_num BETWEEN start_index AND start_index + count - 1
ORDER BY seq_num ASC;

END$$