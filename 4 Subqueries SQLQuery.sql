SELECT emp_name, salary 
FROM employee
WHERE salary > (SELECT AVG(salary) FROM employee);


SELECT dept_name, total_salary
FROM (
    SELECT d.dept_name, SUM(e.salary) AS total_salary
    FROM employee e
    JOIN departments d
    ON e.dept_id = d.dept_id
    GROUP BY d.dept_name
) AS dept_totals
WHERE total_salary = (
    SELECT MAX(total_salary)
    FROM (
        SELECT SUM(e.salary) AS total_salary
        FROM employee e
        JOIN departments d
        ON e.dept_id = d.dept_id
        GROUP BY d.dept_name
    ) AS totals
);


SELECT emp_name, salary
FROM employee
WHERE Salary = (
    SELECT MAX(salary)
    FROM employee
    WHERE Salary < (SELECT MAX(salary) FROM employee)
);


SELECT emp_name
FROM employee
WHERE dept_id = (
   SELECT dept_id
   FROM employee
   WHERE emp_name = 'Taksh'
   );


