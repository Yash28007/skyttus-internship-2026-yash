Select count (*) Total_student from student ;

SELECT AVG(marks) AS average_marks FROM student;

select 
      max(marks) As highest_marks,
      min(marks) As lowest_marks
from Student;

select department, AVG(marks) AS avg_marks
from student
GROUP BY department;

select department, AVG(marks) AS avg_marks
FROM student
GROUP BY department
HAVING AVG(marks) > 70;

