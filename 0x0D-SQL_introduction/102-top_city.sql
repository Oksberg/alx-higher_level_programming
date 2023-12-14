-- imports a table dump in a database, and displays the top 3 cities temperature during July and August ordered by temperature
USE hbtn_0c_0;

\. ./temperatures.sql

SELECT city, AVG(value) AS AVG_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY AVG_temp DESC
LIMIT 3;
