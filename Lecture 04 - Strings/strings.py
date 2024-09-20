
txt = "Hello World"
txt = txt.upper()
length = len(txt)
print(length)
print(txt)


txt = "Hello,Hello,Hello Hello Hello"
txt_lst = txt.split(',')
print(txt_lst)


##############################################
# String Operators
##############################################


txt1 = 'Hello'
txt2 = 'World'

print(txt1 + txt2)
print(txt1)
print(txt2)


txt = "Hello"
print(txt * 5)
print(txt[0])
print(txt[1])
print(txt[4])

print(txt[-5])

print(txt[-3:-1])
print(txt[:3])
print(txt[1:])
print(txt[::-1])
print(txt[10])



##############################################
# String Methods
##############################################

txt1 = ''
txt2 = '  '
print(txt2.strip() == txt1)

first_name = 'john'
last_name = 'doe'

full_name = first_name.capitalize() + " " + last_name.capitalize()
print(full_name)


txt = ' Hello\tWorld '
replaced_txt = txt.replace("\t", '').replace(' ', '')
print(replaced_txt)


txt = 'hello\nworld\nHello\nWorld'
mail = 'Hello\nHow Are you, I have message to you\nBest Regards'
print(mail)



##############################################
# String Format
##############################################



number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))



result = "number1 + number2 = %s" % (number1 + number2)
result = "number1 + number2 = %d" % (number1 + number2)
result = "number1 + number2 = %f" % (number1 + number2)
print(result)

result = "{} + {} = {}".format(number1, number2, number1+number2)
result = "{1} + {2} = {0}".format(number1, number2, number1+number2)
print(result)


result = f"{number1} + {number2} = {number1 + number2}"
result = F"{number1} + {number2} = {number1 + number2}"
print(result)


result = "{number1} + {number2} = {addition}"
print(result.format(number1=number1, number2=number2, addition=number1 + number2))