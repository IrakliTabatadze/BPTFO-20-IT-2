
alter table test alter column first_name type varchar(30)

alter table test alter column first_name set not null

alter table test add column update_date timestamp default '2025-01-17' not null

insert into test(id, first_name) values(1, 'John')




------------------------------------------------------------------------------------------------------------------------------



select
	customers.id,
	customers.idnumber,
	customers.first_name,
	customers.last_name,
	customers.dateofbirth,
	cities.cityname
from customers inner join cities on customers.cityid = cities.id




select
	customers.id,
	customers.idnumber,
	customers.first_name,
	customers.last_name,
	customers.dateofbirth,
	cities.cityname
from customers left join cities on customers.cityid = cities.id



select
	customers.id,
	customers.idnumber,
	customers.first_name,
	customers.last_name,
	customers.dateofbirth,
	cities.cityname
from customers right join cities on customers.cityid = cities.id





select
	customers.id,
	customers.idnumber,
	customers.first_name,
	customers.last_name,
	customers.dateofbirth,
	cities.cityname
from customers full join cities on customers.cityid = cities.id




select
	customers.id,
	customers.idnumber,
	customers.first_name,
	customers.last_name,
	customers.dateofbirth,
	cities.cityname
from customers cross join cities



select
	customers.id,
	customers.idnumber,
	customers.first_name,
	customers.last_name,
	customers.dateofbirth,
	cities.cityname
from customers natural join cities





select
	accounts.id,
	accounts.customeridnumber,
	accounts.accountnumber,
	accounttypes.accounttypename,
	accounts.balance,
	first_name,
	last_name
from accounts
	right join accounttypes on accounts.accounttypeid = accounttypes.id -- შუალედური ცხრილი
	left join customers on accounts.customeridnumber = customers.idnumber






select
	customers.idnumber,
	customers.first_name,
	customers.last_name,
	customers.dateofbirth,
	cities.cityname,
	accounts.accountnumber,
	accounttypes.accounttypename,
	accounts.balance
from customers
	left join cities on customers.cityid = cities.id
	inner join accounts on customers.idnumber = accounts.customeridnumber
	right join accounttypes on accounts.accounttypeid = accounttypes.id
where accounttypename = 'Visa'





