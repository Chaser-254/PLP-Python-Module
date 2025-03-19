# list are used to store multiple data at once
# They are created by placing items inside a bracket []

numbers = [1,2,3,4]
print(numbers)

languages = ["Python", "Swift", "Java"]
print(languages[0])
print(languages[1])
print(languages[2])

my_list = ['p','r','o','g','r','a','m']
print(my_list[2:5])
print(my_list[5:])
print(my_list[:1])
print(languages[-3])

#Adding elements in a list using append()
numbers = [21,34,54,12]
print("Before Append:", numbers)
numbers.append(32)

# Adding items to a list using extend()
prime_numbers = [2,3,5]
print("List1:",prime_numbers)

even_numbers = [4,6,8]
print("List2:", even_numbers)

prime_numbers.extend(even_numbers)

print("List after append:", prime_numbers)

languages[2] = "C++"
print(languages)

# Deleting elements from a list using del() and remove()
languages.remove("C++")
print(languages)

del languages[1]
print(languages)

del languages[0 : 2]
print(languages)

languages.remove("Python")
print(languages)

#Adding elements to a list using insert()
languages.insert(0, "Python")
print(languages)

#Removing elements from a list using pop()
languages.pop(0)
print(languages)

#Removing elements from a list using clear()
languages.clear()
languages.index("Java")
print(languages)

#Counting elements in a list using count()
languages = ["Python", "Swift", "Java", "Java"]
languages.count("Java")

#Sorting elements in a list using sort()
languages.sort()
print(languages)

#Reversing elements in a list using reverse()
languages.reverse()
print(languages)

#Copying elements in a list using copy()
languages = ["Python", "Swift", "Java"]
languages.copy()
print(languages)

#Iterating over a list using for loop
langauges = ["Python", "Swift", "Java"]
for langauge in langauges:
    print(langauge)

#List Comprehension
numbers = [numbers*numbers for numbers in range(1,6)]
print(numbers)