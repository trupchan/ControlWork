# class Person:
#     def __init__(self):
#         self._age = 0
#
#     def set_age(self, age):
#         if age < 0:
#             raise ValueError("Возраст не может быть отрицательным!")
#         self._age = age
#
#     def get_age(self):
#         return self._age
#
# if __name__ == "__main__":
#     p = Person()
#     p.set_age(25)
#     print(p.get_age())
#
#     try:
#         p.set_age(-5)
#     except ValueError as e:
#         print(f"Ошибка: {e}")

#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return "I am an animal"
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
#
# if __name__ == "__main__":
#     dog = Dog("Buddy")
#     cat = Cat("Kitty")
#
#     print(dog.name, dog.speak())
#     print(cat.name, cat.speak())
#
# class Vehicle:
#     def move(self):
#         return "Vehicle is moving"
#
# class Car(Vehicle):
#     def move(self):
#         return "Car is driving"
#
# class Bicycle(Vehicle):
#     def move(self):
#         return "Bicycle is pedaling"
#
#
# def move(vehicle):
#     return vehicle.move()
#
#
# if __name__ == "__main__":
#     car = Car()
#     bike = Bicycle()
#
#     print(move(car))
#     print(move(bike))

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

if __name__ == "__main__":
    rect = Rectangle(10, 5)
    circle = Circle(7)

    print(rect.area())
    print(round(circle.area(), 2))

