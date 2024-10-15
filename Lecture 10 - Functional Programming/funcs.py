###############################################
# Lambda
###############################################

# def plus(x, y):
#     return x + y
#
# print(plus(10, 15))
#
#
# plus_lambda = lambda x, y: x + y
#
# print(plus_lambda(50, 70))


#
# txt_is_digit = lambda txt: txt.isdigit()
#
# for _ in range(3):
#     user_input = input('Enter private number: ')
#
#     if txt_is_digit(user_input):
#         print('Input contains only digits')
#     else:
#         print('Please input correct private number')


# plus_lambda = lambda x=5, y=10: x + y
#
# print(plus_lambda(y=50))


# lst = [lambda arg=x: arg * 10 for x in range(10)]
#
# for func in lst:
#     print(func())


lst = [(lambda arg: arg * 10)(x) for x in range(10)]
print(lst)

empty_lst = []
for x in range(10):
    empty_lst.append((lambda arg: arg * 10)(x))

print(empty_lst)


###############################################
# High priority functions
###############################################

from functools import partial, reduce

# def plus(x, y):
#     return x + y
#
#
# plus_var = partial(plus, x=50)
# print(plus_var(y=20))


# lst = [1, 2, 3]

# fact_lambda = lambda a, b: a * b
#
# factorial = reduce(fact_lambda, range(1, 6))
# print(factorial)


# fact_lambda = lambda a, b: a if a < b else b
# lst = [10, 15, 1, 5, 96, 55, 24]
#
# print(reduce(fact_lambda, lst))




# nums = [1, 2, 3, 4, 5, 6]
#
# power = lambda num: num ** 3
#
# result = map(power, nums)
# print(list(result))



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))



# keys = ['name', 'age', 'city']
# values = ['John', 22, 'New York']
#
# print(list(zip(keys, values)))




###############################################
# Try Except
###############################################

try:
    number1 = int(input('Please input a number: '))
    number2 = int(input('Please input a number: '))

    print(number1 / number2)
except ValueError as e:
    print('Please Input Valid Integer')
    print(e)
except ZeroDivisionError as e:
    print('Cannot divide by zero')
    print(e)
except Exception as e:
    print(e)
else:
    print('Else Block')
finally:
    print('Finally')

print('After Try Except')

