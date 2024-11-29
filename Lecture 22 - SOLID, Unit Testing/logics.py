def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@gmail.com'

    def apply_raise(self):
        self.salary *= 2