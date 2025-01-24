import psycopg2

host = 'localhost'
port = '5432'
user = 'postgres'
password = '123123'
database = 'BPTFO-20-IT-2'

connection = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
print("Connection established")

cursor = connection.cursor()

sql_query = """
    select customers.idnumber, customers.first_name, customers.last_name, cities.cityname
    from customers
    left join cities on customers.cityid = cities.id;
"""

select_one_customer = 'select * from customers where id = 1;'

cursor.execute(select_one_customer)

data = cursor.fetchall()
data = cursor.fetchone()

print(data)


delete_query = 'delete from accounts where id = 1;'

cursor.execute(delete_query)


connection.commit()

cursor.close()
connection.close()

# ORM - Object Related Mapping