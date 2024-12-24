create database Test2 -- მონაცემთა ბაზის შექმნა

drop database test2 -- მონაცემთა ბაზის წაშლა

create table testschema.customer2(id integer not null, first_name varchar(20), description text, price float) -- ცხრილის შექმნა (სქემა აუცილებელი არაა თუ public სქემაში ვქმნით)

insert into customer values(10, 'John', 'this is description', 10.5) -- ერთი ობიექტის ჩაწერა ცხრილში(ყველა სვეტი)

insert into customer(description, first_name) values('This is description', 'Kate'), ('This is description', 'Anna'),('This is description', 'Jack') -- რამდენიმე ობიექტის ჩაწერა ცხრილში (ზოგიერთი სვეტი)

SELECT * FROM public.customer -- ყველა ჩანაწერის წაკითხვა მონაცემთა ბაზიდან