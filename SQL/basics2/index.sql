CREATE TABLE accounts2 (
    account_id INT PRIMARY KEY,
    name VARCHAR(50),
    balance DECIMAL(10, 2),
    branch VARCHAR(50)
);

INSERT INTO accounts2 VALUES
(1, "Adam", 500.00, "Mumbai"),
(2, "Bob", 300.00, "Delhi"),
(3, "Charlie", 700.00, "Banglore"),
(4, "David", 1000.00, "Noida");

SELECT * FROM accounts2;

CREATE INDEX idx_branch ON accounts2(branch);

SHOW INDEX FROM accounts2;

SELECT * FROM accounts2
WHERE branch = 'Mumbai';

CREATE INDEX idx2 ON accounts2(branch, balance);

DROP INDEX idx2 ON accounts2;