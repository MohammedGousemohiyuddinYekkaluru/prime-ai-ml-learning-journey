-- Set autocommit to 0
SELECT @@autocommit;
SET autocommit = 0;

CREATE DATABASE prime;

CREATE TABLE accounts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    balance DECIMAL(10, 2)
);

INSERT INTO accounts
(name, balance)
VALUES
('Adam', 500.00),
('Bob', 300.00),
('Charlie', 1000.00);

-- Transactions
START TRANSACTION;

UPDATE accounts SET balance = balance - 50 WHERE id = 1;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;

COMMIT; --commit
-- ROLLBACK; -- it's just undo the uncommited statements only

-- SavePoints in SQL
START TRANSACTION;

UPDATE accounts SET balance = balance + 1000 WHERE id = 1;
SAVEPOINT after_wallet_topup;

UPDATE accounts SET balance = balance + 10 WHERE id = 1;

ROLLBACK TO after_wallet_topup;

COMMIT;

SELECT * FROM accounts;