delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_tag_sentence`(
IN user_id INT,
IN sentence_id INT,
IN tag_id INT)
BEGIN
# Check if user has already tagged sentence
SELECT COUNT(1)
INTO @count
FROM tag_for_sentence as t
WHERE t.user_id = user_id AND t.sentence_id = sentence_id;

IF NOT @count THEN
    INSERT INTO tag_for_sentence (
        user_id,
        sentence_id,
		tag_id)
    VALUES (
		user_id,
        sentence_id,
		tag_id);
ELSE
    UPDATE tag_for_sentence as t
    SET t.tag_id = tag_id
    WHERE t.user_id = user_id AND t.sentence_id = sentence_id;
END IF;

END$$