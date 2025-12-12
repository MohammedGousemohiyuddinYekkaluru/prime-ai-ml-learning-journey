CREATE TABLE student(
    roll_no INT PRIMARY KEY,
    name VARCHAR(30),
    city VARCHAR(30),
    marks INT
);

INSERT INTO student
(roll_no, name, city, marks)
VALUES
(110, "adam", "Delhi", 76),
(108, "bob", "Mumbai", 65),
(124, "casey", "Pune", 94),
(112, "duke", "Pune", 80);

--1st
SELECT * FROM student
WHERE marks > 75;

--2nd
SELECT DISTINCT city
FROM student;

--or
SELECT city 
FROM student
GROUP BY city;

--3rd
SELECT city, max(marks)
FROM student
GROUP BY city;

--4th
SELECT avg(marks)
FROM student;

--5th
ALTER TABLE student
ADD COLUMN grade VARCHAR(2);

UPDATE student
SET grade = "O"
WHERE marks > 80;

UPDATE student
SET grade = "A"
WHERE marks BETWEEN 70 AND 80;

UPDATE student
SET grade = "B"
WHERE marks BETWEEN 60 AND 70;

SELECT * FROM student;