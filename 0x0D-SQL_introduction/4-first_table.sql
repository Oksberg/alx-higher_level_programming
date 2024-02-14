-- Creates a table, does not fail if already exists.
-- Database name is passed as an argument of
-- the mysql command
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256));
