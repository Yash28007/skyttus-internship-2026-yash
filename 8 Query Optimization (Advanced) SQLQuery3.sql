USE ecommerce_db;

CREATE INDEX orders_customer_id
ON orders (customer_id);

SELECT *
FROM orders
WHERE customer_id = 1;

SET STATISTICS PROFILE ON;
SELECT  c.name, o.amouunt
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;
SET STATISTICS PROFILE OFF;

CREATE NONCLUSTERED INDEX customer_id
ON orders (customer_id);

CREATE NONCLUSTERED INDEX order_customer_id
ON orders (customer_id);

SELECT c.name, o.order_id, o.amouunt
FROM customers AS c
INNER JOIN orders AS o
 ON o.customer_id = c.customer_id
 WHERE o.customer_id = 1;

 select *
 from  orders
 where order_date between ' 2024-01-14' and '2024-05-28';

 select *
 from customers 
 Where city in ('gujarat','delhi');




