delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_tag_sentence`(
IN user_id INT,
IN sentence_id INT,
IN tag_id INT)
BEGIN
SET autocommit = 1;
SET @tagExists = 0;
SET @tag_total = 0;
SET @story_id = 0;
SET @status = 0;

SELECT COUNT(1) into @tagExists
FROM tag_for_sentence ts
WHERE ts.user_id = user_id AND ts.sentence_id = sentence_id AND ts.tag_id is not null;

IF @tagExists = 0 THEN
	INSERT INTO tag_for_sentence (
		user_id,
		sentence_id,
		tag_id)
	VALUES (
		user_id,
		sentence_id,
		tag_id);

    SELECT story_tag_count,
		   assigned_story_id,
		   current_sentence_group_seq,
           sentence_group_size,
		   total_tag_count,
           story.sentence_count
	  INTO
           @story_tag_count,
           @story_id,
           @group_seq,
           @group_size,
           @total_tag_count,
           @story_sentence_count
    FROM user_app_data ud
	INNER JOIN story
        ON story.id = ud.assigned_story_id
    WHERE ud.user_id = user_id;

    SET @story_tag_count = @story_tag_count + 1;
    SET @total_tag_count = @total_tag_count + 1;

    -- Check if user has tagged the last sentence in story
	IF @story_tag_count = @story_sentence_count THEN
        SET @status = 2;
		SET @story_tag_count = 0;
        SET @group_seq = 0;
        -- Assign new story
        call usp_sel_story_to_assign(user_id, @story_id);
    -- Check if user has tagged last sentence in group
    ELSEIF @story_tag_count % @group_size = 0 THEN
        SET @group_seq = @group_seq + 1;
		SET @status = 1;
    END IF;

	UPDATE user_app_data ud
	SET total_tag_count = @total_tag_count,
        story_tag_count = @story_tag_count,
        current_sentence_group_seq = @group_seq,
        assigned_story_id = @story_id
	WHERE ud.user_id = user_id;
ELSE
UPDATE tag_for_sentence ts
SET tag_id = tag_id
WHERE ts.user_id = user_id AND ts.sentence_id = sentence_id;
END IF;


SELECT @total_tag_count as total_tag_count, @status as status, sentence.id, sentence.sentence_txt, sentence.seq_num, ts.tag_id
FROM sentence
INNER JOIN tag_for_sentence ts
    on ts.sentence_id = sentence.id
WHERE sentence.id = sentence_id;

END$$