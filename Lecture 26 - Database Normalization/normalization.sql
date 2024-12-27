-- ყველა ჩანაწერის წაკითხვა(ყველა სვეტი)
select * from customer

-- ყველა ჩანაწერის წაკითხვა რომელთა სახელიც არის Anna(ყველა სვეტი)
select * from customer where first_name = 'Anna'

-- ყველა ჩანაწერის წაკითხვა რომელთა სახელიც არის Anna(მხოლოდ არჩეული სვეტები)
select description as "desc", first_name as name from customer where first_name = 'Anna'




-- ცხრილის შექმნა ავტომატურად ზრდადი მთავარი გასაღებით
create table customerinfo(
	id serial primary key,
	first_name varchar(20),
	dateofbirth date,
	create_date timestamp,
	city varchar(10)
)


-- ინფორმაციის ჩაწერა ცხრილში(primary key-ს შემთხვევაში მისი მნიშვნელობა არ უნდა შევიყვანოთ)
insert into customerinfo(first_name, dateofbirth, create_date) values('John', '1995-08-11', '2025-12-27 20:37'),
('Kate', '2000-08-11', '2025-12-27 20:37'),
('Jake', '2005-09-12', '2025-12-27 20:37')


insert into customerinfo(first_name, dateofbirth, create_date, city) values('Kate', '2000-08-11', '2025-12-27 20:37', 'Tbilisi')


-- id მნიშვნელობით ფილტრაცია
select * from customerinfo where id=2

-- თარიღის მიხედვით ფილტრაცია
select * from customerinfo where dateofbirth > '1995-01-01' and dateofbirth < '2001-01-01'
select * from customerinfo where dateofbirth > '1995-01-01' or dateofbirth < '2001-01-01'
select * from customerinfo where dateofbirth between '1995-01-01' and '2001-01-01'

-- მრავალი პარამეტრით ფილტრაცია
select * from customerinfo where dateofbirth > '1995-01-01' and dateofbirth < '2001-01-01' and first_name = 'John'
select * from customerinfo where dateofbirth > '1995-01-01' and dateofbirth < '2001-01-01' and first_name like 'John%'
select * from customerinfo where dateofbirth > '1995-01-01' and dateofbirth < '2001-01-01' and first_name like '%Doe'
select * from customerinfo where dateofbirth > '1995-01-01' and dateofbirth < '2001-01-01' and first_name like '%n%'

-- დასელექტებული მნიშვნელობის სორტირება
select * from customerinfo order by dateofbirth asc
select * from customerinfo order by dateofbirth desc

-- ჩანაწერების მხოლოდ გარკვეული რაოდენობით წაკითხვა
select * from customerinfo order by dateofbirth desc limit 3


-- ჩანაწერების განახლება
update customerinfo set create_date = '2025-12-27'

update customerinfo set create_date = '2025-12-27 21:18:15' where id > 4

-- ჩანაწერების წაშლა
delete from customerinfo where id > 4
delete from customerinfo

-- ცხრილის გასუფთავება
truncate customer

-- ცხრილის წაშლა
drop table customerinfo