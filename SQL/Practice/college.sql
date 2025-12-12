-- Active: 1765374014918@@127.0.0.1@3306@college
CREATE DATABASE IF NOT EXISTS college;

USE college;

CREATE TABLE teacher (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    subject VARCHAR(50),
    salary INT
);

INSERT INTO teacher
(roll_no, name, subject, salary)
VALUES
(23, "ajay", "math", 50000),
(47, "bharat", "english", 60000),
(18, "chetan", "chemistry", 45000),
(9, "divya", "physics", 75000);

--1st
SELECT * FROM teacher
WHERE salary > 55000;

--2nd
ALTER TABLE teacher
CHANGE COLUMN salary ctc INT;

--3rd
UPDATE teacher
SET ctc = ctc + ctc * 0.25;

--4th
ALTER TABLE teacher
ADD COLUMN city VARCHAR(25) DEFAULT "Gurgaon";

--5th
ALTER TABLE teacher
DROP COLUMN ctc;

SELECT * FROM teacher;

