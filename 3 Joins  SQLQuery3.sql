CREATE DATABASE company_db;

USE company_db;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

INSERT INTO departments VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance');

INSERT INTO employee VALUES
(101, 'yash', 1, 60000),
(102, 'aryan', 2, 75000),
(103, 'krish', 3, 90000),
(104, 'taksh', 2, 72000),
(105, 'prince', NULL, 95000);

SELECT e.emp_name, d.dept_name
FROM employee e
LEFT JOIN departments d
ON e.dept_id = d.dept_id;

SELECT emp_name, salary
FROM employee
WHERE salary > 70000;

SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employee e
JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM employee e
JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 2;

SELECT emp_name
FROM employee
WHERE dept_id IS NULL;
