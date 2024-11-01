#####################################################
# Decorators
#####################################################

def decorator(func):
    def wrapper(*args, **kwargs):
        print('Decorator Function: x+10, y+10')
        x = args[0] + 10
        y = args[1] + 10
        if x > 0 and y > 0:
            return func(x, y)
        else:
            return 'Please Input Only Positive Numbers'
    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print('Decorator2 Function: x+100, y+100')
        x = args[0] + 100
        y = args[1] + 100
        return func(x, y)
    return wrapper


@decorator2
@decorator
def calculate(x, y):
    print(f'x = {x}, y = {y}')
    return x + y

print(calculate(10, -5))


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def message():
    print("Hello")

@repeat(3)
def message2():
    print("Hello2")

message()
message2()



#####################################################
# Functors
#####################################################

class Functor:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = [self.func(i) for i in args]
        print(result)

def square(x):
    return x ** 2

functor = Functor(square)
functor(1, 2, 3, 4, 5)


#####################################################
# Descriptor
#####################################################


class Descriptor:
    def __get__(self, instance, owner):
        print(f'Getting Value: {instance.name}, {instance.age}')
        return instance.name

    def __set__(self, instance, value):
        print(f'Setting Value: {instance.name} = {value}')
        instance.name = value

    def __delete__(self, instance):
        print(f'Deleting Value: {instance.name}')
        del instance.name

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    descriptor = Descriptor()

person1 = Person('John', 25)
print(person1.descriptor)
person1.descriptor = 'Kate'
print(person1.descriptor)
del person1.descriptor
print(person1.descriptor)






class PositiveNumber:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f'attr: {instance.__dict__[self.name]}')


class Rectangle:
    width = PositiveNumber()
    height = PositiveNumber()

    def __init__(self, width, height):
        self.width = width
        self.height = height


rect = Rectangle(height=10, width=20)
print(rect.width)



#####################################################
# __new__, MetaClass
#####################################################


def init(self, brand, model):
    self.brand = brand
    self.model = model

def return_values(self):
    return f'Brand: {self.brand}, Model: {self.model}'

Car = type('Car', (object,), {
    '__init__': init,
    'return_values': return_values
})


car = Car(brand='Mercedes', model='C500')

print(car.return_values())


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def return_values(self):
        return f'Brand: {self.brand}, Model: {self.model}'

car1 = Car('Mercedes', 'C550')
print(car1.return_values())




class Car(type):
    def __new__(cls, name, bases, dct):
        instance = super().__new__(cls, name, bases, dct)
        return instance

class ElectricCar(metaclass=Car):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def return_values(self):
        return f'Brand: {self.brand}, Model: {self.model}'

print(type(ElectricCar))
elCar = ElectricCar('Tesla', 'Roadster')
print(elCar.return_values())