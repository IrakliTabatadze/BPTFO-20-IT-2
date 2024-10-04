# import test
# from test import satesto_variable

# print(test.satesto_variable2)

import random

######################################
# Function
######################################

def print_something():
    print("First Line")
    print("Second Line")
    print("Third Line")
    print("Fourth Line")
    print("Fifth Line")

print_something()
print_something()
print_something()
print_something()



def add_numbers(number1, number2):
    # print(number1 + number2)
    return number1 + number2, number1 - number2


add_numbers(10, 20)
add_numbers(25, 25)
add_numbers(11, 12)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

added_nums, minus_nums = add_numbers(a, b)
print(added_nums)
print(minus_nums)




def add(x=125, y=165):
    return x + y


added_numbers = add()
print(added_numbers)



def add(q=0, w=0, e=0, r=0, t=0, y=0, u=0, i=0, o=0):
    print(f'q = {q}, w = {w}, e = {e}, r = {r}')
    return q + w + e + r + t + y + u + i + o

added_number = add(e=10, w=25, r=25)
print(added_number)


def student(first_name, last_name, age, courses):
    return {'first_name': first_name, 'last_name': last_name, 'age': age, 'courses': courses}

student1 = student(first_name='John', last_name='Johnson', courses=['Python', 'C++'], age=25)
print(student1)



def add(operator, *args, **kwargs):
    print(kwargs)
    if operator == '+':
        sum_of_number = 0
        for number in args:
            sum_of_number += number

        return sum_of_number

    elif operator == '-':
        difference_of_number = 0
        for number in args:
            difference_of_number -= number

        return difference_of_number

added_numbers = add('+', 15, 1200, 1400, 1500, number=125, number2=200)
print(added_numbers)



def palyndrome(txt: str, txt2: str='', lst: list=[]) -> str:
    txt = txt.lower()
    if txt == txt[::-1]:
        return True
    else:
        return False

is_palyndrome = palyndrome('saas')
if is_palyndrome:
    print("It is Palyndrome")
else:
    print("It is not Palyndrome")

