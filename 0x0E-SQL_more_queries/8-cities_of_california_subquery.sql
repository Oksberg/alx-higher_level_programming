-- Lists all the cities of California found in hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id
SELECT id, name FROM cities
WHERE state_id=(SELECT id FROM states WHERE name='California')
ORDER BY id ASC;
