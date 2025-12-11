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

CREATE TABLE posts (
    id INT PRIMARY KEY,
    content VARCHAR(100),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);


