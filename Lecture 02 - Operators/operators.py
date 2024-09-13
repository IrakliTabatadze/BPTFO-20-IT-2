################################################
# Arithmetic Operators
################################################

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

plus = number1 + number2
minus = number1 - number2
multiplication = number1 * number2
division = number1 / number2
floor_division = number1 // number2
modulus = number1 % number2
exponantiation = number1 ** number2

print("number1 + number2 = ", plus)
print("number1 - number2 = ", minus)
print("number1 * number2 = ", multiplication)
print("number1 / number2 = ", division)
print("number1 // number2 = ", floor_division)
print("number1 % number2 = ", modulus)
print("number1 ** number2 = ", exponantiation)


################################################
# Assignment Operators
################################################

number = 10

number = number + 10
print(number)

number = int(input("Enter a number: "))

number += 10
print("Plus:", number)

number2 = int(input("Enter a number: "))
number2 -= 10
print("Minus:", number2)

number3 = int(input("Enter a number: "))
number3 *= 10
print("Multiplication:", number3)

number4 = int(input("Enter a number: "))
number4 /= 10
print("Division:", number4)

number5 = int(input("Enter a number: "))
number5 //= 3
print("Exponential:", number5)

number6 = int(input("Enter a number: "))
number6 %= 10
print("Modulus:", number6)

number7 = int(input("Enter a number: "))
number7 **= 2
print("Power:", number7)


################################################
# Comparing Operators
################################################

number1 = 30
number2 = 20

print("number1 > number2:", number1 > number2) # gt
print("number1 < number2:", number1 < number2) # lt
print("number1 >= number2:", number1 >= number2) # gte
print("number1 <= number2:", number1 <= number2) # lte
print("number1 == number2:", number1 == number2)
print("number1 != number2:", number1 != number2)

txt_1 = "Hello World!!!"
txt_2 = "Hello World!!"
print("txt_1 == txt_2:", txt_1 == txt_2)


################################################
# Logic Operators
################################################

x = 4

# True and True = True
# True and False = False
# False and True = False
# False and False = False


# True or True = True
# True or False = True
# False or True = True
# False or False = False

print(x<20 and x>5)
print(5 < x < 20)

print(x>20 or (x>5 and x < 10))

not_operator = not(x>20 or (x>5 and x < 10))
print(not_operator)


################################################
# Identity Operators
################################################

x = 5

print(x is 5)

print(id(x))
print(id(5))

x = 'a'
aa = x * 2
print(id(aa))
print(id('aa'))
print('aa' is aa)
print('aa' is not aa)


################################################
# Membership Operators
################################################

txt = "Hello World!!!"

print("!!!!" in txt)
print("!!!" not in txt)


################################################
# if/elif/else
################################################


age = int(input("Enter your age: "))

if age >= 18:
    print("You are a teenager.")

print("After If Statement")





number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))


if number1 > number2:
    print('number1 Greater Than number2')
elif number1 < number2:
    print('number1 Less Than number2')
elif number1 == number2:
    print('number1 Equal to number2')


if number1 > number2:
    print('number1 Greater Than number2')
elif number1 < number2:
    print('number1 Less Than number2')
else:
    print('number1 Equal to number2')


if number1 >= number2:
    print('number1 Greater Than Or Equal number2')
else:
    print('number1 Less Than number2')



################################################
# Ternary Operator
################################################

number = int(input("Enter a number: "))
result = "Zero" if number == 0 else "Not Zero"
print(result)
