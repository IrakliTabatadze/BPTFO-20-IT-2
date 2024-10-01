#########################################
# Tuples
#########################################

empty_tuple = ()
print(type(empty_tuple))


one_element_tuple = ("Hello", )
print(one_element_tuple)

filled_tuple = (10, 11, 21, 'Hello', .5, [10, 14, 15])
filled_tuple2 = (500, 1000, 2000)
print(filled_tuple[-1][2])
print(filled_tuple[2:5])
print(filled_tuple[:4])
print(filled_tuple[1:])

if 50 in filled_tuple:
    print(filled_tuple)

for item in filled_tuple:
    print(item)

print(filled_tuple + filled_tuple2)
print(filled_tuple)
print(filled_tuple * 3)
print(filled_tuple)

filled_tuple[-1].append("New Information")
print(filled_tuple)

lst = [10, 15, 20]

lst[0] += 10
print(lst)

filled_tuple[0] = filled_tuple[0] + 20
print(filled_tuple)


dct = {'name': 'john', 'age': 25}
print(dct.items())


number1, number2 = 10, 20
print(number1, number2)

new_tuple = ('First Element', 'Second Element', 'Third Element', 'Fourth Element', 'Fifth Element', 'Sixth Element')
first_element, second_element, *other_elements, last_element = new_tuple
print(first_element)
print(second_element)
print(other_elements)
print(last_element)


for i, j in enumerate(new_tuple, start=1):
    print(i, j)


print(new_tuple.index('Third Element'))
print(new_tuple.count('First Element'))


#########################################
# Set
#########################################

empty_set = set()
print(type(empty_set))


filled_set = {10, 5, 9, 15, 25, False, 0, True, 1}
print(filled_set)

for item in enumerate(filled_set):
    print(item)




filled_set = {10, 5, 9, 15, 25, False, 0, True, 1}

filled_set.add('Hello')
filled_set.add('Hi')
filled_set.remove('H')
filled_set.pop()
filled_set.pop()
print(filled_set)


# (1,2,3,4,5) (4,5,6,7,8)
#
# (4, 5) # თანაკვეთა
# (1,2,3,4,5,6,7,8) # გაერთიანება
# (1,2,3) # გამოკლება

filled_set1 = {10, 5, 9, 15, 25, False, 0, True, 1, 'Hello', 'Hi', 'Python'}
filled_set2 = {11, 13, 14, 23, 24, False, 0, True, 1, 'Hello', 'Hi', 'Python'}

difference = filled_set1.difference(filled_set2)
filled_set1.difference_update(filled_set2)
print(filled_set1)
print(difference)

print(filled_set1.symmetric_difference(filled_set2))


intersection = filled_set1.intersection(filled_set2)
filled_set1.intersection_update(filled_set2)
print(intersection)
print(filled_set1)


union = filled_set1.union(filled_set2)
print(union)


#########################################
# FrozenSet
#########################################

filled_set1 = {10, 5, 9, 15, 25, False, 0, True, 1, 'Hello', 'Hi', 'Python'}
filled_set2 = {11, 13, 14, 23, 24, False, 0, True, 1, 'Hello', 'Hi', 'Python'}


frozen1 = frozenset(filled_set1)
frozen2 = frozenset(filled_set2)

print(frozen1)
print(frozen2)

frozen_difference = frozen1.difference(frozen2)
print(frozen_difference)



frozen_for_dict = frozenset({10, 15})
dct = {frozen_for_dict: "Hello Frozenset"}

print(dct[frozen_for_dict])
