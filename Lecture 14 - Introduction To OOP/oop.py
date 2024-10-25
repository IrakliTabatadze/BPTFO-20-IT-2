
txt = str('Hello World')
print(type(txt))

txt1 = 'Hello'
txt2 = 'World'

txt1.upper()


class Human:
    legs = 2
    eyes = 2
    nose = 1
    ears = 2

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.last_name = 'Doe'

    @staticmethod
    def walking():
        print('Walking!!!')

    def talking(self):
        print(f'{self.name} can Talking!!!')

    @classmethod
    def running(cls):
        print(f'{cls.eyes} Running!!!')


human1 = Human('John', 25)
print(human1.legs)
human2 = Human('Kate', 26)
print(human2.legs)

human1.walking()
human2.walking()

print(type(human1))
print(type(human2))

human1.eyes = 3
print(human1.eyes)
print(human2.eyes)

print(human1.name, human1.age)
print(human2.name, human2.age)
print(human1.ears, human2.ears)

human1.talking()
human2.talking()




##################################################
# Encapsulation
##################################################


# Public, Protected, Private


class PublicEncapsulation:
    public_cls_attr = 'public_attr'

    def public_method(self):
        print(self.public_cls_attr)

public_obj = PublicEncapsulation()
public_obj.public_method()


class ProtectedEncapsulation:
    _protected_cls_attr = '_protected_cls_attr'

    def _protected_method(self):
        print('Protected')

protected_obj = ProtectedEncapsulation()
protected_obj._protected_method()
print(protected_obj._protected_cls_attr)



class PrivateEncapsulation:
    __private_cls_attr = '__private_cls_attr'

    def __private_method(self):
        print(self.__private_cls_attr)

private_obj = PrivateEncapsulation()
print(private_obj.__private_cls_attr)
private_obj.__private_method()

####################################################
# Inheritance
####################################################


class Animal:
    legs = 4

    def __init__(self, name):
        self.name = name



class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def meow(self):
        print(f'{self.name} is meow!')


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f'{self.name} is bark!')

cat = Cat('Loki', 'White')
print(cat.legs)
cat.meow()

dog = Dog('Fluffy', 'Boxer')
print(dog.legs)
dog.bark()



####################################################
# Multiple Inheritance
####################################################

class Mother:
    def __init__(self, name, hair_color):
        self.name = name
        self.hair_color = hair_color

    def greet(self):
        print(f"{self.name} says Hello")

    def bake_cookies(self):
        print(f"{self.name} bakes best cookies")


class Father:
    def __init__(self, name, eye_color):
        self.name = name
        self.eye_color = eye_color

    def greet(self):
        print(f"{self.name} says Hello")

    def tell_jokes(self):
        print(f"{self.name} says funny jokes")

class Child(Mother, Father):
    def __init__(self, name, hair_color, eye_color, profession):
        Mother.__init__(self, name, hair_color)
        Father.__init__(self, name, eye_color)
        self.profession = profession


child = Child('Anna', 'Black', 'Blue', 'Developer')
child.bake_cookies()
child.tell_jokes()

mother = Mother()
father = Father()



####################################################
# Polymorphism
####################################################


class Shape:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def area(self):
        print("This is Shape Class Method")


class Rectangle(Shape):
    def area(self):
        width, height = self.dimensions
        return width * height

class Cirlce(Shape):
    def area(self):
        radius = self.dimensions[0]
        return 3.14 * radius ** 2


rect = Rectangle([10, 20])
circle = Cirlce([10])

rect_area = rect.area()
circle_area = circle.area()

print(rect_area)
print(circle_area)