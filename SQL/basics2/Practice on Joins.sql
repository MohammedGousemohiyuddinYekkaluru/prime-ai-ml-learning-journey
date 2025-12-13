-- Write SQL Command to display the exclisive joins

--Left exclusive join
select * 
FROM customers c
LEFT JOIN orders o 
ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;

--Right exclusive join
select *
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id
WHERE c.customer_id IS NULL;