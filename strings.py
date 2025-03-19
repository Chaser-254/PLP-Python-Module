#strings in python are ordered sequence of characters
#Creating a string
string1 = 'Hello, World!'
print(string1)

#Accessing elements in a string
print(string1[0])

#Accessing elements in a string using negative indexing
print(string1[-1])

#Accessing elements in a string using slicing
print(string1[7:12])

#Accessing elements in a string using slicing with a step
print(string1[0:12:2])

#Accessing elements in a string using slicing with a negative step
print(string1[12:0:-2])

#string operation
string2 = 'Python'
string3 = 'Programming'
print(string2 + string3)

#Repeating a string
print(string2 * 3)

#Checking if a character exists in a string using in
print('P' in string2)
