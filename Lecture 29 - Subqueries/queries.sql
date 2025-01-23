
select * from customers where cityid is not NULL


select cityid, sum(income), max(income), min(income), avg(income)
from customers
group by cityid
having cityid in (1, 4, NULL)


select
	cities.cityname,
	avg(income)
from customers
	left join cities on customers.cityid = cities.id
group by cities.cityname having cityname in ('Tbilisi', 'Telavi')



select * from customers where idnumber in (select distinct(customeridnumber) from accounts)
select distinct(customeridnumber) from accounts



create or replace function set_create_date()
returns trigger as $$
	BEGIN
		NEW.create_date = NOW();
		return NEW;
	END
$$ language plpgsql;



create trigger set_create_date_trigger
before insert on customers
for each row
execute function set_create_date();


insert into customers(idnumber, first_name, last_name, cityid) values('101010105','Jack', 'Doe', 2),('101010106','Jack', 'Doe', 2),('101010107','Jack', 'Doe', 2),('101010108','Jack', 'Doe', 2)


create or replace function set_update_date()
returns trigger as $$
	BEGIN
		NEW.update_date = NOW();
		return NEW;
	END
$$ language plpgsql;


create trigger set_update_date_trigger
before update on customers
for each row
execute function set_update_date();



update customers set income = 10000 where idnumber='101010106'