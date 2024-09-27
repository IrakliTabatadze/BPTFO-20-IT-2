#######################################
# Dict Creation
#######################################

empty_dict = {}
empty_dict2 = dict()

print(empty_dict)
print(empty_dict2)


lst = [10, 11, 12]
lst[0] = 25
print(lst)


filled_dict = {"name": "John", 'age': 20, 'profession': 'Developer'}

print(filled_dict['profession'])
filled_dict['courses'] = ['Python', 'Java', 'C++']
print(filled_dict)
filled_dict['courses'] = "Student's courses"
filled_dict['courses'].append("Appended Information")
print(filled_dict)



#######################################
# Dict Methods
#######################################

filled_dict = {"name": "John", 'age': 20, 'profession': 'Developer'}
print(filled_dict['courses'])
selected_info = filled_dict.get('name', 'Key Not Found')
print(selected_info)
print(filled_dict.keys())
print(filled_dict.values())

print(filled_dict.items())

tupl = ('name', 'john')
key, value = tupl
print(key, value)

for i, j in [[1, 2], [3, 4]]:
    print(i, j)

for key, value in filled_dict.items():
    print(f'{key}: {value}')

for i in filled_dict:
    print(i, filled_dict[i])



print(filled_dict)

filled_dict.setdefault('first_name', 'Kate')
filled_dict.setdefault('first_name', 'John')

print(filled_dict)

filled_dict2 = {'name': 'Kate', 'age': 20, 'profession': 'Seller', 'courses': ['Python', 'Java']}

filled_dict.update(filled_dict2)
print(filled_dict)
filled_dict['name'] += ' Doe'

print(filled_dict)
filled_dict.clear()

print(filled_dict)
print(filled_dict.pop('name'))
print(filled_dict.popitem())


print(filled_dict)
filled_dict2 = filled_dict.copy()
print(id(filled_dict2))
print(id(filled_dict))
filled_dict.popitem()
print(filled_dict)
print(filled_dict2)


#######################################
# Nested Dicts
#######################################


products = {
    'electronics': {
        'laptops': {
            '1001': {'brand': 'Apple', 'price': 2500, 'quantity': 1},
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
    }
}

# print(products['electronics']['phones']['2001']['price'])


full_price = 0

for key, value in products.items():
    # print(f'{key}: {value}')
    for key1, value1 in value.items():
        # print(f'{key1}: {value1}')
        for key2, value2 in value1.items():
            # print(f'{key2}: {value2}')
            price = 0
            quantity = 0
            for key3, value3 in value2.items():
                # print(f'{key3}: {value3}')

                if key3 == 'price':
                    price = value3
                if key3 == 'quantity':
                    quantity = value3

                if price > 0 and quantity > 0:
                    full_price += price * quantity
                    price = 0
                    quantity = 0


print(full_price)