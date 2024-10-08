
####################################################
# LEGB
####################################################
import math

def circle_area(pi):
    def whole_area(radius):
        return pi * radius ** 2
    # print(whole_area)
    return whole_area

circle = circle_area(math.pi)
print(circle(10))



x = 10 # Global Variable

def legb():
    # global x
    # x = x + 1
    x = 25 # Enclosed Variable
    def nested_func():
        # y = x + 150
        # print(y)
        # x = 50 # Local Variable
        global x
        x += 10
        print(x)
    nested_func()


legb()



x = 10

for i in range(10):
    x = 25
    for j in range(10):
        x += 10




def square(x):
    return x ** 2

def cube(x):
    return x ** 3


lst = [square, cube]

for func in lst:
    print(func.__name__, func(5))





####################################################
# Recursive Functions
####################################################

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)


# გლობალური დიქტი
# ფუნქცია - პროფილის შექმნისთვის(სახელს, გვარს)
# შეინახეთ გლობალურ დიქტში


global_lst = []

def create_profile(first_name, last_name, **kwargs):
    global global_lst

    global_dict = {}

    global_dict.setdefault('first_name', first_name)
    global_dict.setdefault('last_name', last_name)

    for key, value in kwargs.items():
        global_dict.setdefault(key, value)
    global_lst.append(global_dict)
    print(global_lst)


create_profile('John', 'Smith', date_of_birth = '2024-01-15')
create_profile('John', 'Smith', email = 'test@gmail.com')
create_profile('John', 'Smith', email = 'test2@gmail.com', date_of_birth='2024-01-15', profession='Developer')
