###########################################
# Regex
###########################################


import re

text = 'Python is the best programming language in the world'

pattern = r'[aeiou]'
pattern = r'P.*n'
matches = re.findall(pattern, text)

print(matches)

text = re.sub(pattern, '{ხმოვანი}', text)
print(text)



###########################################
# Lists
###########################################

empty_list = []
empty_list2 = list()


print(empty_list)
print(empty_list2)


hobbies = ['Programming', 'Music', 'Walking', True, False, 1, 2, 3, 5.5]
print(len(hobbies))

hobbies += ['Coding']
print(hobbies)

hobbies *= 3
print(len(hobbies))
print(hobbies)

print('Programming' not in hobbies)


print(hobbies[2])
print(hobbies[-1])
print(hobbies[1:3])
print(hobbies[:3])
print(hobbies[2:])
print(hobbies[::-1])


###########################################
# List Methods
###########################################

hobbies1 = ['Programming', 'Programming','Programming', 'Music', 'Walking', True, False, 1, 2, 3, 5.5]
hobbies2 = ['Programming', 'Music', 'Walking', True, False, 1, 2, 3, 5.5]

hobbies1.clear()
music_index = hobbies.index('Music')

hobbies1.append("Appended Information")
hobbies1.append(['new list', 'new list2'])
hobbies1.extend(hobbies2)

hobbies1.insert(20, 'Inserted Information')


for hobby in hobbies1:
    if hobby == 'Programming':
        hobbies1.remove(hobby)

for i in range(len(hobbies1)):
    if 'Programming' in hobbies1:
        hobbies1.remove('Programming')

print(hobbies1.remove('Programming'))

last_item = hobbies1.pop(5)
print(last_item)


new_hobbies = hobbies1
hobbies1.pop()

print(id(hobbies1))
print(id(new_hobbies))


questions = ['question1', 'question2', 'question3', 'question4', 'question5']
new_quest = questions.copy()

new_quest.remove('question4')
new_quest.remove('question2')
new_quest.remove('question1')
new_quest.remove('question3')
new_quest.remove('question5')

if len(new_quest) == 0:
    print("You finished")

print(new_quest)
print(questions)


lst = [10, 11, 8, 6, 12]
lst.sort(reverse=True)
print(lst)


###########################################
# List Comperhension
###########################################

integer_list = [i for i in range(1, 11) if i % 2 == 0]

print(integer_list)


new_integers = []

for i in range(1, 11):
    if i % 2 == 0:
        new_integers.append(i)

print(new_integers)



###########################################
# Matrix
###########################################

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in matrix:
    print(i)

print(matrix[2][3])

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column])