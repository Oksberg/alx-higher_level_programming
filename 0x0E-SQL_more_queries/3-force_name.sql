-- Creates the table force_name on my MYSQL server
-- If force_name already exists, the script doesn't fail
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
