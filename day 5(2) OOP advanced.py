class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class ElectricCar(Car):
    def move(self):
        return "Electric car is running silently"

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

def calculate_area(shape):
    return shape.area()

class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Insufficient balance"

class CurrentAccount(Account):
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, salary):
        self.salary = salary

class Manager(Person, Employee):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Employee.__init__(self, salary)

class SecureAccount:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Student(Teacher):
    def __init__(self, name, subject, grade):
        super().__init__(name, subject)
        self.grade = grade

class MusicPlayer:
    def play(self):
        return "Playing music"

class Spotify(MusicPlayer):
    def play(self):
        return "Playing music on Spotify"

class Base:
    def __init__(self):
        self.value = 10

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.value += 5