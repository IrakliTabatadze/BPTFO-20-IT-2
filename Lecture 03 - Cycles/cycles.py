#################################################
# Iterator
#################################################

txt = 'Hello World!'
iterator_txt = iter(txt)


i = next(iterator_txt)
print(i)
i = next(iterator_txt)
print(i)
i = next(iterator_txt)
print(i)
i = next(iterator_txt)
print(i)
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))


#################################################
# While
#################################################

number = 10

while number > 0:
    number -= 1

    if number == 5:
        # continue
        break
    print(number)
else:
    print("While cycle finished successfully")

print("Done")


a = 10
b = 20

counter = 1

while a < b:
    print(counter, "Infinite Cycle")
    counter += 1


while True:
    print(True)



while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break
    else:
        continue



#################################################
# For
#################################################

txt = 'Hello World!'

for i in txt:
    print(i)


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
iter_lst = iter(lst)

i = next(iter_lst)
print(i)
i = next(iter_lst)
print(i)
i = next(iter_lst)
print(i)
i = next(iter_lst)
print(i)
i = next(iter_lst)
print(i)
i = next(iter_lst)
print(i)
i = next(iter_lst)
print(i)

for i in range(10, 20, 2):
    print(i)

for i in range(20, 10, -1):
    print(i)


x = 20

while x >= 10:
    print(x)
    x -= 0.5


#################################################
# Random
#################################################

import random

random_number = random.random()
print(random_number)


random_number = random.randint(50, 100)
print(random_number)

random_number = random.randrange(50, 100)
print(random_number)


print(random.randint(50, 100))
print(random.randint(50, 100))
print(random.randint(50, 100))
print(random.randint(50, 100))
print(random.randint(50, 100))
print(random.randint(50, 100))