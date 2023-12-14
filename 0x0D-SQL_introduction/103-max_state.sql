-- imports table dump in a database, and then displays the max temperature of each state ordered by State name
USE hbtn_0c_0;

\. ./temperatures.sql

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
