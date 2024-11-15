import requests

cars_url = 'https://crudcrud.com/api/efb11ff5219a47f59a15d32ffa53ed39/cars'

response = requests.get(cars_url)

response = requests.get(cars_url + '/67377f4a00892d03e8b4cd19').json()

print(response.json())

car = {'brand': 'Ford', 'model': 'Mustang'}


response = requests.post(cars_url, json=car)
print(response.json())


car = {'brand': 'Lamborghini', 'model': 'Countach'}

response = requests.put(cars_url + '/67377f4a00892d03e8b4cd19', json=car)
print(response)


response = requests.delete(cars_url + '/67377f4a00892d03e8b4cd19')
print(response)