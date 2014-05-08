delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sentence_validate`(
IN user_id INT,
IN sentence_id INT,
IN tag_id INT)
BEGIN
SET autocommit = 1;
SET @legit = TRUE;

SELECT assigned_story INTO @story_id
FROM user_app_data as ud
WHERE ud.user_id = user_id;

-- Check if sentence belongs to story
SELECT sentence.story_id INTO @s_id
FROM sentence
WHERE sentence.id = sentence_id;
IF @story_id != @s_id OR @s_id IS NULL THEN
    SET @legit = FALSE;
END IF;

-- Check valid sequence order
SELECT sentence.seq_num INTO @next_seq_num
FROM sentence
LEFT OUTER JOIN tag_for_sentence as ts
    ON sentence.id = ts.sentence_id
WHERE sentence.story_id = @story_id
  AND ts.tag_id IS NULL
ORDER BY seq_num ASC
LIMIT 1;
SELECT sentence.seq_num INTO @seq_num
FROM sentence
WHERE sentence.id = sentence_id;
IF @seq_num > @next_seq_num THEN
    SET @legit = FALSE;
END IF;

-- Check valid tag_id
SELECT COUNT(1) into @tag
FROM tag
WHERE tag.id = tag_id;
IF @tag = 0 THEN
    SET @legit = FALSE;
END IF;

SELECT @legit as legit;

END$$






