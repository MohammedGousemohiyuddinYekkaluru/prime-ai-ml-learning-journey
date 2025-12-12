-- Active: 1765374014918@@127.0.0.1@3306@college
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    FirstName VARCHAR(30),
    LastName VARCHAR(30),
    Department VARCHAR(50),
    Salary INT,
    HireDate DATE
);

INSERT INTO employee
(`EmpID`, `FirstName`, `LastName`, `Department`, `Salary`, `HireDate`)
VALUES
(101, "Alice", "Johnson", "IT", 6500, '2020-03-15'),
(102, "Mark", "Rivera", "HR", 4800, '2019-07-22'),
(103, "Sophia", "Lee", "Finance", 7200, '2021-01-10'),
(104, "Daniel", "Kim", "IT", 5800, '2018-11-05'),
(105, "Emma", "Brown", "Marketing", 5300, '2022-04-18'),
(106, "Liam", "Patel", "Finance", 6900, '2020-09-29'),
(107, "Olivia", "Garcia", "HR", 4600, '2017-06-30'),
(108, "Noah", "Thompson", "IT", 7500, '2023-02-12'),
(109, "Ava", "Martinez", "Marketing", 5100, '2019-12-02'),
(110, "Ethan", "Davis", "Finance", 8000, '2016-05-14');

--1st --> Display every employee and all their data
SELECT * FROM employee;

--2nd --> FirstName, LastName, and Salary of every employee
SELECT FirstName, LastName, Salary
FROM employee;

--3rd --> employee who works in IT Dept.,
SELECT * FROM employee
WHERE `Department` = "IT";
