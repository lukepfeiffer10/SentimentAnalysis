delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_sentence_group`(
IN user_id int(11))
BEGIN

SELECT assigned_story_id,
       current_sentence_group_seq,
       sentence_group_size
INTO
       @assigned_story_id,
       @group_seq,
       @group_size
FROM user_app_data uad
WHERE uad.user_id = user_id;

SET @start_seq = @group_seq * @group_size;

SELECT sentence.id, sentence.sentence_txt, sentence.seq_num, ts.tag_id
FROM sentence
LEFT OUTER JOIN tag_for_sentence ts
    on ts.sentence_id = sentence.id AND
       ts.user_id = user_id
WHERE sentence.story_id = @assigned_story_id AND
      sentence.seq_num BETWEEN @start_seq AND @start_seq + @group_size - 1;

END$$