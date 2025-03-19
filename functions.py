#function in python is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

def function1():
    print("Hello, World!")
function1()
#A function is defined using the def keyword, followed by the function name, parentheses, and a colon. The code block within every function starts with an indentation and ends with the first unindented line. The code block is executed when the function is called.

#Types of functions in Python
#There are two types of functions in Python:
#1. Built-in functions
#2. User-defined functions

#Built-in functions
#Built-in functions are those functions that are already defined in Python. Some of the built-in functions in Python are:
#1. print()
#2. input()
#3. len()
#4. range()
#5. int()
#6. float()
#7. str()
#8. list()
#9. tuple()

#User-defined functions
#User-defined functions are those functions that are defined by the user. The syntax for defining a user-defined function is:
#def function_name():
#    code block
#    code block
#    code block

#Calling a function
#To call a function, you simply write the function name followed by parentheses. For example:
#function_name()
def greet(name):
    """
    This function greets the user
    """
    print("Hello, " + name)
greet("World")

#Arguments in functions
#Arguments are the values that are passed to a function when it is called. There are four types of arguments in Python:
#1. Default arguments
#2. Keyword arguments
#3. Arbitrary arguments
#4. Arbitrary keyword arguments

#Default arguments
#Default arguments are those arguments that take a default value if no argument value is passed during the function call. The syntax for defining a default argument is:
#def function_name(argument = value):
def greet(name = "World"):
    """
    This function greets the user
    """
    print("Hello, " + name)
greet()

#Keyword arguments
#Keyword arguments are those arguments that are preceded by an identifier when we pass them to a function. The order of the arguments does not matter in keyword arguments. The syntax for defining a keyword argument is:
#def function_name(argument1, argument2):
def introduce(name,age):
    """
    This function introduces the user
    """
    print("Hello, my name is " + name + " and I am " + age + " years old")
introduce(age = "20", name = "John")    

#Arbitrary arguments
#Arbitrary arguments are those arguments that are preceded by an asterisk (*) when we pass them to a function. The syntax for defining arbitrary arguments is:
#def function_name(*argument):  
def greet(*names):
    """
    This function greets all the users
    """
    for name in names:
        print("Hello, " + name)
greet("John", "Jane", "Jack")

#Arbitrary keyword arguments
#Arbitrary keyword arguments are those arguments that are preceded by two asterisks (**) when we pass them to a function. The syntax for defining arbitrary keyword arguments is:
#def function_name(**argument):

def greet(**names):
    """
    This function greets all the users
    """
    for key, value in names.items():
        print("Hello, " + key + " " + value)
greet(a = "John", b = "Jane", c = "Jack")

#Return statement in functions
#The return statement is used to exit a function and return a value. The syntax for defining a return statement is:
#def function_name():
#    code block

def add(a, b):
    """
    This function adds two numbers
    """
    return a + b
result = add(2, 3)

#Scope of variables in functions
#The scope of a variable is the part of the program where the variable is accessible. There are two types of variable scopes in Python:
#1. Local scope
#2. Global scope
