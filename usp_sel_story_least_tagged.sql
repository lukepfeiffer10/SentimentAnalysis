delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `usp_sel_story_least_tagged`()
BEGIN
SELECT st.story_title, st.id
FROM story AS st
LEFT OUTER JOIN sentance AS se
    ON st.id = se.story_id
LEFT OUTER JOIN tag_for_sentance AS ts
    ON ts.sentance_id = se.id
GROUP BY st.story_title
ORDER BY COUNT(ts.tag_id) ASC
LIMIT 1;
END$$

