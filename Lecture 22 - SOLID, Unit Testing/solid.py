# S O L I D

# S - Single Responsibility Principle

class TextFileManager:

    def write_txt(self):
        pass

    def read_txt(self):
        pass

class ZipFileManager:
    def compress(self):
        pass

    def decompress(self):
        pass


# O - Open Closed Principle

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# L - Liskov Substitution Principle

class KitchenApp:
    def on(self):
        pass

    def off(self):
        pass

class Juicer(KitchenApp):
    def on(self):
        pass

    def off(self):
        pass

class KitchenAppWithTemperature(KitchenApp):
    def on(self):
        pass
    def off(self):
        pass

    def set_temperature(self, temperature):
        pass



class Toster(KitchenAppWithTemperature):
    def on(self):
        pass
    def off(self):
        pass
    def set_temperature(self, temperature):
        pass

class Fridge(KitchenAppWithTemperature):
    pass


# I - Interface Segregation Principle

class Printer:
    def printing(self):
        pass


class Scanner:
    def scanner(self):
        pass


class PrinterDevice(Printer):
    def printing(self):
        pass

class ScannerDevice(Scanner):
    def scanner(self):
        pass

class MultifunctionalDevice(Printer, Scanner):
    def printing(self):
        pass

    def scanner(self):
        pass


# D - Dependency Inversion Principle

# class Logger:
#     def logs(self, message):
#         with open('test.txt', 'a') as f:
#             pass
#
#
# class Calculator:
#     def __init__(self):
#         self.logger = Logger()
#
#     def plus(self, a, b):
#         result = a + b
#         self.logger.log(f'{a} + {b} = {result}')


from abc import ABC, abstractmethod


class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message):
        pass

class Logger(LoggerInterface):
    def log(self, message):
        with open('test.txt', 'a') as f:
            pass

class Calculator:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger


    def plus(self, a, b):
        result = a + b
        self.logger.log(f'{a} + {b} = {result}')


calculator = Calculator(Logger())