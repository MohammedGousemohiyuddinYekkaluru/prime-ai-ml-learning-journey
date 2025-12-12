-- Active: 1765374014918@@127.0.0.1@3306@instagram
CREATE DATABASE IF NOT EXISTS instagram;

USE instagram;

CREATE TABLE user (
    id INT,
    age INT,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE,
    followers INT DEFAULT 0,
    following INT DEFAULT 0,
    CONSTRAINT CHECK (age >= 13),
    PRIMARY KEY (id)
);

INSERT INTO user
(id, age, name, email, followers, following)
VALUES
(1, 14, "adam", "adam@yahoo.in", 123, 145),
(2, 15, "bob", "bob123@gnail.com", 200, 200),
(3, 16, "casey", "casey@email.com", 300, 306),
(4, 17, "donald", "donald@gmail.com", 200, 105);

SELECT id, name, age FROM `user`;
SELECT DISTINCT age FROM `user`; --selects unique ages
SELECT * FROM `user`;

--selecting data on conditions using WHERE Clause
SELECT name, followers FROM `user` WHERE followers >= 200;

SELECT name, age FROM `user` WHERE age + 1 = 18;

--selecting data using Operators
SELECT name, age, followers
FROM user
WHERE age > 15 or followers > 200;

SELECT name, age, followers
FROM user
WHERE age BETWEEN 15 AND 17;

SELECT name, age, email
FROM user
WHERE email IN ("donald@gmail.com", "bob123@gnail.com", "abc@gmail.com");

INSERT INTO `user`
(id, age, name, email, followers, following)
VALUES
(5, 14, "eve", "eve@yahoo.in", 400, 145),
(6, 16, "farah", "farah@mail.in", 10000, 1045);

SELECT name, age, followers, email
FROM user
WHERE age IN (14, 16);

SELECT name, age, followers, email
FROM user
WHERE age NOT IN (14, 16);

--Limit clause
SELECT name, age, followers, email
FROM user
WHERE age > 14
LIMIT 2;

--Order by clause
SELECT name, age, followers
FROM user
ORDER BY followers ASC; --ASC -> Ascending order/DESC -> Descening order

--Aggregate Functions
SELECT max(age) FROM `user`; --max
SELECT min(age) FROM `user`;

SELECT avg(age) FROM `user`;

SELECT COUNT(age) FROM `user` WHERE age >= 14;

SELECT sum(followers) FROM `user`;

--Group by Clause
SELECT age, count(id) FROM `user` GROUP BY age;

SELECT age, max(followers) FROM `user` GROUP BY age;

--Having Clause -> it applies after Group by
--General order
SELECT age, max(followers) 
FROM `user` 
GROUP BY age 
HAVING max(followers) > 200
ORDER BY max(followers) DESC;

--UPDATE Table
UPDATE `user`
SET followers = 600
WHERE age = 16

SELECT name, age, followers FROM `user` WHERE age = 16;

--DELETE Table
DELETE FROM instauser
WHERE age =  14;

--ALTER Table -> to change the schema

--Add column
ALTER TABLE `user`
ADD COLUMN city VARCHAR(25) DEFAULT "Delhi";

--Drop column
ALTER TABLE `user`
DROP COLUMN email;

--Rename Table
ALTER TABLE `user`
RENAME TO instaUser;

--Change column name (rename)
ALTER TABLE instauser
CHANGE COLUMN followers subscribers INT DEFAULT 0;

--Modify Column
ALTER TABLE instauser
MODIFY subscribers INT DEFAULT 5;

--TRUNCATE Table
TRUNCATE TABLE instauser;

DROP TABLE instauser;




CREATE TABLE posts (
    id INT PRIMARY KEY,
    content VARCHAR(100),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

INSERT INTO posts
(id, content, user_id)
VALUES
(101, "Hello World", 3),
(102, "Bye Bye", 1),
(103, "Hello guys", 3);

SELECT * FROM posts;

DROP TABLE posts;


