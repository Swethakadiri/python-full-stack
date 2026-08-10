CREATE DATABASE offices;
USE offices;

CREATE TABLE emp(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(40),
    dept_id INT,
    dept_name VARCHAR(10)
);

INSERT INTO emp VALUES
(2, "swetha", 20, "MCA"),
(3, "sandy", 30, "CSE"),
(4, "radhika", 40, "EEE"),
(5, "naresh", 50, "BCA"),
(6, "sandhya", 20, "MPC");

SELECT * FROM emp;

ALTER TABLE emp ADD COLUMN marks INT;

UPDATE emp
SET marks = 80
WHERE emp_id = 2;

DELIMITER //
CREATE PROCEDURE find_employee(
    IN p_departments INT
)
BEGIN
    SELECT *
    FROM emp
    WHERE dept_id >= p_departments;
END //
DELIMITER ;
CALL find_employee(30);



DELIMITER //
CREATE PROCEDURE count_employees(
    OUT total INT
)
BEGIN
    SELECT COUNT(*) INTO total
    FROM emp;
END //
DELIMITER ;
SET @employee_count = 0;
CALL count_employees(@employee_count);
SELECT @employee_count;