SELECT * FROM customers;

CREATE VIEW view1 AS
SELECT customer_id, nmae FROM customers;

SELECT * FROM view1
WHERE nmae = "Alice";

CREATE VIEW view2 AS
SELECT c.customer_id, c.nmae, o.order_id
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

SELECT * FROM view2;