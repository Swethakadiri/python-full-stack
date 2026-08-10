create database students_info;
use students_info;
CREATE TABLE students_management(
    student_id INT,
    student_name VARCHAR(30),
    course VARCHAR(40),
    teacher VARCHAR(50),
    teacher_num BIGINT
);

INSERT INTO students_management VALUES
(10, 'swetha', 'python', 'mahesh', 2759478248),
(20, 'sandhya', 'python', 'suresh', 1679803767),
(30, 'radhika', 'java', 'naresh', 3657687988),
(50, 'sandy', 'java', 'kumar', 89635637667),
(60, 'siri', 'python', 'ramesh', 6479837939);

create table students(
      student_id INT PRIMARY KEY,
      student_name VARCHAR(40)
);     

create table courses(
       course VARCHAR(30) PRIMARY KEY,
       teacher VARCHAR(30),
       teacher_num int
);

create table enrollment(
         student_id INT,
         course VARCHAR(30),
         PRIMARY KEY(student_id,course)
);

create table teachers(
      teacher_id INT PRIMARY KEY,
      teacher_name VARCHAR(30),
      phone VARCHAR(30)
);
create table course(
     course varchar(30) PRIMARY KEY,
     teacher_id int
);