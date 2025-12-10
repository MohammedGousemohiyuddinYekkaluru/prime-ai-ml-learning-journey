CREATE DATABASE test_db;

USE test_db;

CREATE TABLE student(
    roll_no INT,
    name VARCHAR(30),
    age INT
);

INSERT INTO student
VALUES
(101, "adam", 12),
(102, "bob", 14);

SELECT * FROM student;