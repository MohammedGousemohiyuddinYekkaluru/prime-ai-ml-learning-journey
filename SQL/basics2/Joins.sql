CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    nmae VARCHAR(50),
    city varchar(50)
);

INSERT INTO customers VALUES
(1, "Alice", "Mumbai"),
(2, "Bob", "Delhi"),
(3, "Charlie", "Banglore"),
(4, "David", "Mumbai");

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount INT
);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700);

--inner join
SELECT c.customer_id, o.order_id, c.nmae
FROM customers as c
INNER JOIN orders as o 
ON c.customer_id = o.customer_id;

--Left join
SELECT *
FROM customers c
LEFT JOIN orders o 
ON c.customer_id = o.customer_id;

--Right join --> just opposite to the Left join
SELECT *
FROM customers c
RIGHT JOIN orders o 
ON c.customer_id = o.customer_id;

--Outer Join --> union of left and right join
SELECT *
FROM customers c
LEFT JOIN orders o 
ON c.customer_id = o.customer_id
UNION
SELECT *
FROM customers c
RIGHT JOIN orders o 
ON c.customer_id = o.customer_id;

--Cross join
SELECT *
FROM customers
CROSS JOIN orders;

--Self join
SELECT *
FROM customers A 
JOIN customers B
ON A.customer_id = B.customer_id;