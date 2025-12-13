-- Active: 1765374014918@@127.0.0.1@3306@instagram
--using WHERE
SELECT *
FROM orders
WHERE amount > (
    SELECT AVG(amount)
    FROM orders
);

--using SELECT
SELECT nmae, (
    SELECT COUNT(*)
    FROM orders o
    WHERE o.customer_id = c.customer_id
) AS order_count
FROM customers c;

--using FROM
SELECT
    summary.customer_id,
    summary.avg_amount
FROM (SELECT customer_id, AVG(amount) as avg_amount
FROM orders
GROUP BY customer_id)
as summary;


