create database students;
use students;
create table toppers(
        name VARCHAR(40),
        marks INT,
        department VARCHAR(30)
);
insert into toppers values("swetha",98,"MCA"),
("sandhya",99,"BCA"),
("radhika",97,"MCA"),
("sandy",96,"BCA");

select * from toppers;

CREATE VIEW topper AS SELECT  name,marks from toppers;
select * from topper;
create view topper1 as select * from toppers where marks>96;
select * from topper1;
create view topper2 as select name,marks from toppers where marks>96;
select * from topper2;