from models import session, Customer, City, Accounts, AccountTypes
from datetime import datetime


customers = session.query(Customer).all()

print(customers)

for customer in customers:
    print(customer.first_name, customer.last_name, customer.idnumber)


customers_id_lt_20 = session.query(Customer).filter(Customer.id < 20).all()

for customer in customers_id_lt_20:
    print(customer.id, customer.first_name)


customer_id1 = session.query(Customer).filter(Customer.id == 1).first()

print(customer_id1)



customers_filter_by_create = session.query(Customer.id, Customer.create_date).filter(Customer.create_date < datetime(2025, 1, 21, 21, 5)).all()

for customer in customers_filter_by_create:
    print(customer)



customer_cities = session.query(Customer, City.cityname).outerjoin(City, Customer.cityid == City.id).all()
print(customer_cities)


for customer, city in customer_cities:
    print(customer.id, city.cityname)


customer_cities_accounts = session.query(Customer, City, Accounts).join(City, Customer.cityid == City.id).join(Accounts, Customer.idnumber == Accounts.customeridnumber).all()
print(customer_cities_accounts)


for customer,city,accounts in customer_cities_accounts:
    print(customer.idnumber, city.cityname, accounts.accountnumber)




city = City('New York')

session.add(city)
session.commit()


city1 = City('New York')
city2 = City('New York')

cities = [city1, city2]

session.add_all(cities)
session.commit()



city = session.query(City).filter(City.id==8).first()

city.cityname = 'New Jersey'

session.commit()


city = session.query(City).filter(City.id==8).first()
session.delete(city)
session.commit()