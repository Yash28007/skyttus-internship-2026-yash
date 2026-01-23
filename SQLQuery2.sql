create database StudentDB;
use StudentDB;
create table Student (
	Student_ID INT,
	Name VARCHAR(50),
	department VARCHAR(30),
	year INT,
	marks INT);

INSERT INTO Student VALUES
(1, 'yash', 'IT', 6, 95),
(2, 'Meet', 'CSC', 5, 90),
(3, 'Nisarg', 'BSC', 4, 78),
(4, 'Aryan', 'MCA', 4, 88),
(5, 'krish', 'BCA', 2, 92);


-- Display all student records
SELECT * FROM Student;

-- Display only name and department
SELECT name, department FROM student;

-- Display students with marks greater than 75
SELECT * FROM Student
WHERE marks > 75;

-- Display students from the IT department
SELECT * FROM Student
WHERE department = 'IT';

--Sort students by marks in descending order
SELECT * FROM Student
ORDER BY marks DESC;

--Display Top 3 Scorers
SELECT TOP 3 * FROM Student
ORDER BY marks DESC;