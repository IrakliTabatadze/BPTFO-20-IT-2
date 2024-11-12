################################################
# Serialization
################################################

import json

products = {
    "electronics": {
        "laptops": {
            "1001": {"brand': 'Apple', 'price': 2500, 'quantity': 1},
                     '1002': {'brand': 'HP', 'price': 1500, 'quantity': 10}
                     },
            'phones': {
                '2001': {'brand': 'Apple', 'price': 2000, 'quantity': 15},
                '2002': {'brand': 'Samsung', 'price': 2000, 'quantity': 10},
            }
        },
        'clothes': {
            'shirts': {
                '3001': {'brand': 'Nike', 'price': 500, 'quantity': 1},
                '3002': {'brand': 'Adidas', 'price': 500, 'quantity': 10}
            },
            'pants': {
                '4001': {'brand': 'Levis', 'price': 500, 'quantity': 50},
                '4002': {'brand': 'Lee', 'price': 500, 'quantity': 50},
            }
        },
        'electronics3': {
            'laptops': {
                '1001': {'brand': 'Apple', 'price': 2500, 'quantity': 1},
                '1002': {'brand': 'HP', 'price': 1500, 'quantity': 10}
            },
            'phones': {
                '2001': {'brand': 'Apple', 'price': 2000, 'quantity': 15},
                '2002': {'brand': 'Samsung', 'price': 2000, 'quantity': 10},
            }
        },
        'clothes3': {
            'shirts': {
                '3001': {'brand': 'Nike', 'price': 500, 'quantity': 1},
                '3002': {'brand': 'Adidas', 'price': 500, 'quantity': 10}
            },
            'pants': {
                '4001': {'brand': 'Levis', 'price': 500, 'quantity': 50},
                '4002': {'brand': 'Lee', 'price': 500, 'quantity': 50},
            }
        },
        'electronics2': {
            'laptops': {
                '1001': {'brand': 'Apple', 'price': 2500, 'quantity': 1},
                '1002': {'brand': 'HP', 'price': 1500, 'quantity': 10}
            },
            'phones': {
                '2001': {'brand': 'Apple', 'price': 2000, 'quantity': 15},
                '2002': {'brand': 'Samsung', 'price': 2000, 'quantity': 10},
            }
        },
        'clothes2': {
            'shirts': {
                '3001': {'brand': 'Nike', 'price': 500, 'quantity': 1},
                '3002': {'brand': 'Adidas', 'price': 500, 'quantity': 10}
            },
            'pants': {
                '4001': {'brand': 'Levis', 'price': 500, 'quantity': 50},
                '4002': {'brand': 'Lee', 'price': 500, 'quantity': 50},
            }
        },
        'electronics1': {
            'laptops': {
                '1001': {'brand': 'Apple', 'price': 2500, 'quantity': 1},
                '1002': {'brand': 'HP', 'price': 1500, 'quantity': 10}
            },
            'phones': {
                '2001': {'brand': 'Apple', 'price': 2000, 'quantity': 15},
                '2002': {'brand': 'Samsung', 'price': 2000, 'quantity': 10},
            }
        },
        'clothes1': {
            'shirts': {
                '3001': {'brand': 'Nike', 'price': 500, 'quantity': 1},
                '3002': {'brand': 'Adidas', 'price': 500, 'quantity': 10}
            },
            'pants': {
                '4001': {'brand': 'Levis', 'price': 500, 'quantity': 50},
                '4002': {'brand': 'Lee', 'price': 500, 'quantity': 50},
            }
        }
    }
}
print(products)

json_products = json.dumps(products)
print(json_products)

with open('products.json', 'w') as json_file:
    json_file.write(json_products)
    json.dump(products, json_file, indent=4)

from faker import Faker
from random import randint

fake = Faker()


class Student:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession


student1 = Student(fake.first_name(), randint(20, 50), 'Developer')
student2 = Student(fake.first_name(), randint(20, 50), 'Developer')
student3 = Student(fake.first_name(), randint(20, 50), 'Developer')

students = [student1, student2, student3]
print(student)


def custom_serializer(obj):
    if isinstance(obj, Student):
        return {'name': obj.name, 'age': obj.age, 'profession': obj.profession}
    raise TypeError('Object must be of type Student')


json_string = json.dumps(students, default=custom_serializer)

print(json_string)

with open('students.json', 'w') as json_file:
    json.dump(students, json_file, default=custom_serializer, indent=4)

################################################
# Deserialization
################################################
import json

json_products = '''{
    "electronics": {
        "laptops": {
            "1001": {"brand": "Apple", "price": 2500, "quantity": 1},
            "1002": {"brand": "HP", "price": 1500, "quantity": 10}
        },
        "phones": {
            "2001": {"brand": "Apple", "price": 2000, "quantity": 15},
            "2002": {"brand": "Samsung", "price": 2000, "quantity": 10}
        }
    },
    "clothes": {
        "shirts": {
            "3001": {"brand": "Nike", "price": 500, "quantity": 1},
            "3002": {"brand": "Adidas", "price": 500, "quantity": 10}
        },
        "pants": {
            "4001": {"brand": "Levis", "price": 500, "quantity": 50},
            "4002": {"brand": "Lee", "price": 500, "quantity": 50}
        }
    },
    "electronics3": {
        "laptops": {
            "1001": {"brand": "Apple", "price": 2500, "quantity": 1},
            "1002": {"brand": "HP", "price": 1500, "quantity": 10}
        },
        "phones": {
            "2001": {"brand": "Apple", "price": 2000, "quantity": 15},
            "2002": {"brand": "Samsung", "price": 2000, "quantity": 10}
        }
    },
    "clothes3": {
        "shirts": {
            "3001": {"brand": "Nike", "price": 500, "quantity": 1},
            "3002": {"brand": "Adidas", "price": 500, "quantity": 10}
        },
        "pants": {
            "4001": {"brand": "Levis", "price": 500, "quantity": 50},
            "4002": {"brand": "Lee", "price": 500, "quantity": 50}
        }
    }
}'''

json_products = '[{"name": "Lee", "price": 20.50, "quantity": 1}, {"name": "Lee", "price": 20.50, "quantity": 1}]'

print(type(json_products))
try:
    python_data = json.loads(json_products)
except json.decoder.JSONDecodeError:
    print("Invalid type in json string")

print(type(python_data))
print(python_data['name'])
for product in python_data:
    print(product)

with open('products.json', 'r') as json_file:
    try:
        data = json.load(json_file)
        print(data['electronics'])
    except json.decoder.JSONDecodeError as e:
        print(e)

json_students = '[{"name": "Lisa", "age": 20, "profession":"Developer"}, {"name": "Lisa", "age": 20, "profession":"Developer"}]'


class Student:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def __str__(self):
        return self.name


def custom_deserializer(json_obj):
    return Student(json_obj['name'], json_obj['age'], json_obj['profession'])


python_data = json.loads(json_students, object_hook=custom_deserializer)
print(python_data)

with open('students.json', 'r') as json_file:
    students = json.load(json_file, object_hook=custom_deserializer)
    print(students)
