-- Creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 has only SELECT privilege in hbtn_0d_2
-- user has password user_0d_2_pwd
-- The script doesn't fail if hbtn_0d_2 exists
-- The script doesn't fail if hbtn_0d_2 exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
