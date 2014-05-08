SELECT sentence_id, tag_id
FROM story
INNER JOIN sentence
    on story.id = sentence.story_id
INNER JOIN tag_for_sentence as t
	on sentence.id = t.sentence_id
WHERE story.id = 13;