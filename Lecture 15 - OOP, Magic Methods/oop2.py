#################################################
# Property, Getter, Setter, Deleter
#################################################


class PublicEncapsulation:

    def __init__(self, name, age):
        self.name = name
        self.age = age


public_obj = PublicEncapsulation('John', 25)

print(public_obj.name)
print(public_obj.age)

public_obj.name = 'Kate'
public_obj.age = 30

print(public_obj.name)
print(public_obj.age)

del public_obj.name

print(public_obj.name)
print(public_obj.age)


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.getter
    def name(self):
        return self.__name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age


person1 = Person("John", 25)
print(person1.name)
print(person1.age)

person1.name = "Kate"
print(person1.name)

person1.age = 30
print(person1.age)

del person1.name
del person1.age
print(person1.name)

#######################################################
# Abstract Class
#######################################################

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def calculate_area(self, radius):
        return 3.14 * radius ** 2


class Rectangle(Shape):
    def calculate_area(self, width, height):
        return width * height


circle = Circle()
print(circle.calculate_area(10))

rect = Rectangle()
print(rect.calculate_area(10, 20))

shape = Shape()
shape.calculate_area()


#######################################################
# Method Overload
#######################################################

class Calculator:
    def add(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b
            return f'The sum of {a} and {b} is: {result}'
        elif isinstance(a, str) and isinstance(b, str):
            result = a + b
            return f'Concatenating {a} and {b}: {result}'
        else:
            raise TypeError('Input only integers or strings')


calc = Calculator()
print(calc.add(10, 20))
print(calc.add(10.5, 20.5))
print(calc.add('Hello', 'World'))
print(calc.add('True', 10))

from multipledispatch import dispatch


class Calculator:
    @dispatch(int, int)
    def add(self, x, y):
        result = x + y
        return f'The sum of integer numbers {x} and {y} is: {result}'

    @dispatch(int, int, int)
    def add(self, x, y, z):
        result = x + y + z
        return f'The sum of integer numbers {x} and {y} and {z} is: {result}'

    @dispatch(float, float)
    def add(self, x, y):
        result = x + y
        return f'The sum of float numbers {x} and {y} is: {result}'

    @dispatch(str, str)
    def add(self, a, b):
        result = a + b
        return f'Concatenating {a} and {b}: {result}'


calc = Calculator()
print(calc.add(10, 20))
print(calc.add(10.5, 20.5))
print(calc.add('Hello', 'World'))


# print(calc.add(10, 20, 30))


#######################################################
# Magic Methods
#######################################################

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('Unsupported Operand')
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y


vector1 = Vector(1, 2)
vector2 = Vector(1, 2)
vector3 = vector1 + vector2
print(vector3.x, vector3.y)
print(vector1 == vector2)


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'Person({self.first_name}, {self.last_name})'


person1 = Person("John", "Doe")
print(person1)

# frozen_set = frozenset([1, 2, 3, 4])
# print(frozen_set)
