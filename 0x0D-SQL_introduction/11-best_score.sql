-- Lists all records with a score >= 10 in the table
-- second_table of a database passed as an argument of -- the mysql command.
-- Results should display both the score and the name
-- in that order, and ordered by the score (top first).
SELECT score, name FROM second_table
WHERE score>=10
ORDER BY score DESC;
