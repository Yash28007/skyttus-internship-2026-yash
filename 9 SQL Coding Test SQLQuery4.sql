CREATE DATABASE CompanyDB;

USE CompanyDB;


CREATE TABLE employees1 (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    hire_date DATE,
    email VARCHAR(50)
);

CREATE TABLE employees_a1 (
    emp_id INT,
    emp_name VARCHAR(50)
);

CREATE TABLE employees_b1 (
    emp_id INT,
    emp_name VARCHAR(50)
);

CREATE TABLE logs1 (
    id INT,
    value VARCHAR(10)
);

INSERT INTO employees1 VALUES
(1, 'Taksh', 50000, '2025-01-10', 'taksh@gmail.com'),
(2, 'Yash', 60000, '2023-10-15', 'yash@gmail.com'),
(3, 'Krish', 60000, '2023-08-20', 'krish@gmail.com'),
(4, 'Dhruv', 45000, '2024-11-01', 'dhruv@gmail.com'),
(5, 'aryan', 50000, '2024-01-10', 'arayan@gmail.com'); 

INSERT INTO employees_a1 VALUES
(1, 'Dhruv'),
(2, 'Krish'),
(3, 'Yash');

INSERT INTO employees_b1 VALUES
(2, 'Dhruv'),
(3, 'Yash'),
(4, 'aryan');

INSERT INTO logs1 VALUES
(1, 'A'),
(2, 'A'),
(3, 'A'),
(4, 'B'),
(5, 'B'),
(6, 'C');

--Nth Highest Salary (Example: 3rd)
DECLARE @N INT = 3;

SELECT salary
FROM (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees1
) t
WHERE rnk = @N;

--Remove Duplicate Records (by email)
WITH cte AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY emp_id) AS rn
    FROM employees1
)
DELETE FROM cte
WHERE rn > 2;

--Common Records in Two Tables
SELECT * FROM employees_a1
INTERSECT
SELECT * FROM employees_b1;

--Employees Hired in Last 6 Months
SELECT *
FROM employees1
WHERE hire_date >= CAST(DATEADD(MONTH, -6, GETDATE()) AS DATE);

--Continuous Duplicate Values
SELECT *
FROM (
    SELECT *,
           LAG(value) OVER (ORDER BY id) AS prev_value
    FROM logs1
) t
WHERE value = prev_value;