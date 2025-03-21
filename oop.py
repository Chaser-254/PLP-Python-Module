#Object Oriented Programming in python helps us to build and model a complex systems by traeting real world entities as objects within the program
# 1. **Class**: A blueprint for creating objects.
# 2. **Object**: An instance of a class.
# 3. **Encapsulation**: Bundling data (attributes) and methods (functions) together.
# 4. **Inheritance**: Creating a new class from an existing class.
# 5. **Polymorphism**: Using a single interface to represent different types.
# 6. **Abstraction**: Hiding implementation details and exposing only the necessary parts.


### 1. **Class and Object**
# Defining a class
class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def introduce(self):  # Method
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Creating an object (instance of the class)
person1 = Person("Alice", 25)
print(person1.introduce())  # Output: Hi, I'm Alice and I'm 25 years old.

### 2. **Encapsulation**
# Encapsulation example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

# Using encapsulation
account = BankAccount("John", 1000)
account.deposit(500)
print(account.get_balance())

### 3. **Inheritance**
# Inheritance example
class Animal:
    def speak(self):
        return "I make a sound."

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())


### 4. **Polymorphism**
# Polymorphism example
class Bird:
    def fly(self):
        return "I can fly!"

class Penguin(Bird):
    def fly(self):
        return "I can't fly, but I can swim!"

def show_flying_ability(bird):
    print(bird.fly())

sparrow = Bird()
penguin = Penguin()

show_flying_ability(sparrow)
show_flying_ability(penguin)


### 5. **Abstraction**
from abc import ABC, abstractmethod
# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(10, 5)
print(rect.area())
print(rect.perimeter())