create table AccountTypes(id serial primary key, accounttypename varchar(30) not null)

insert into accounttypes(accounttypename) values('Visa'), ('Master Card'), ('Amex'), ('ვადიანი ანაბარი')


create table Cities(id serial primary key, CityName varchar(30) not null)

insert into cities(cityname) values('Tbilisi'), ('Batumi'), ('Qutaisi'), ('Telavi')


create table customers(
	id serial primary key,
	idnumber varchar(11) not null,
	first_name varchar(30) not null,
	last_name varchar(30) not null,
	dateofbirth date,
	cityid integer,
	zipcode varchar(4),
	street varchar(50),
	housenumber integer,
	income float
	)

insert into customers(idnumber, first_name, last_name, cityid, housenumber, income) values(
	'12345678', 'John', 'Doe', 4, 15, 2000
), ('87654321', 'Kate', 'Smith', 1, 10, 1500),
	('12121212', 'Anna', 'Doe', 1, 12, 1000)



create table accounts(id serial primary key,
	customeridnumber varchar(11) not null,
	accountnumber varchar(50) not null,
	accounttypeid integer not null,
	balance float not null
	)

insert into accounts(customeridnumber, accountnumber, accounttypeid, balance) values
('12345678', 'GE00BG00000012345678', 3, 555.55),
('12345678', 'GE00BG00000012345777', 1, 1000),
('12121212', 'GE00BG00000065421234', 2, 1500),
('19191919191', 'GE00BG00000065421234', 2, 1500)



alter table customers add constraint customers_cities_id_fk foreign key (cityid) references cities(id)

alter table accounts add constraint account_id_fk foreign key (accounttypeid) references accounttypes(id)

alter table accounts add constraint idnumber_fk foreign key (customeridnumber) references customers(idnumber)

alter table customers add constraint unique_idnumber unique (idnumber)




---------------------------------------------------------------------------------------------------------------------------


select *, substr(accountnumber, 5, 2) as BANK_INITIALS from accounts


select min(balance) from accounts

select max(balance) from accounts

select max(balance), min(balance) from accounts

select max(id), min(id) from accounts


select avg(balance) from accounts


select count(*) from customers

select count(dateofbirth) from customers


select count(distinct(customeridnumber)) from accounts


select concat(concat(concat(first_name, '.'), last_name), '@ITStep.org') as full_name from customers







