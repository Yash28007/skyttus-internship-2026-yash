CREATE DATABASE ecommerce_db;
USE ecommerce_db

CREATE TABLE CUSTOMERS (
    customer_id INT PRIMARY KEY,
    name varchar(100) NOT NULL,
    city varchar(50),
);


CREATE TABLE products (
    product_id INT PRIMARY KEY,
        product_name varchar(100) NOT NULL,
        price DECIMAL(10, 2) NOT NULL
);


CREATE TABLE orders (
    order_id INT PRIMARY KEY,
        customer_id INT,
        order_date DATE,
        amouunt DECIMAL(10, 2),
        FOREIGN KEY (customer_id) REFERENCES CUSTOMERS(customer_id)
        );


        CREATE TABLE order_items (
        order_id INT,
        product_id INT,
        quatitty INT NOT NULL,
        PRIMARY KEY (order_id, product_id),
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
        );


INSERT INTO CUSTOMERS (customer_id, name, city) VALUES
(1, 'YASH PATEL','GUJARAT'),
(2, 'KRISH PATEL', 'MUMBAI'),
(3, 'TAKSH PATEL', 'DELHI');

INSERT INTO products (product_id, product_name, price) VALUES
(1, 'Laptop', 800.00),
(2, 'Smartphone', 500.00),
(3, 'Tablet', 300.00);

INSERT INTO orders (order_id, customer_id, order_date, amouunt) VALUES
(1, 1, '2024-01-15', 1300.00),
(2, 2, '2024-02-20', 800.00),
(3, 3, '2024-03-10', 300.00);

INSERT INTO order_items (order_id, product_id, quatitty) VALUES
(1, 1, 1),
(1, 2, 1),
(2, 2, 1),
(3, 3, 1);


SELECT C.customer_id, C.name, COUNT(O.order_id) AS total_orders
FROM customers C
LEFT JOIN orders O ON C.customer_id = O.customer_id
GROUP BY C.customer_id, C.name;


SELECT C.CUSTOMER_ID, C.NAME
FROM CUSTOMERS C
LEFT JOIN orders O ON C.CUSTOMER_ID = O.CUSTOMER_ID
WHERE O.ORDER_ID IS NULL;


SELECT p.product_id, p.product_name, 
       SUM(oi.quantity) AS total_quantity_sold
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC;

--MONTHLY SALES REPORT

SELECT 
  YEAR(order_date) AS year,
  MONTH(order_date) AS month,
  SUM(amouunt) AS total_sales
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;


--CUSTOMER WITH TOTAL PURCHASE   

SELECT 
  C.customer_id,
  C.name,
  SUM(O.amouunt) AS total_purchase
  FROM CUSTOMERS C
  JOIN orders O ON C.customer_id = O.customer_id
  GROUP BY C.customer_id, C.name
  HAVING SUM(O.amouunt) > 100;


  --TOP 3 CITIES BY REVENUE


  SELECT
   C.city,
    SUM(O.amouunt) AS total_revenue
    FROM CUSTOMERS C
    JOIN orders O ON C.customer_id = O.customer_id
    GROUP BY C.city
    ORDER BY total_revenue DESC;

