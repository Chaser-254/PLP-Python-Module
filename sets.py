#sets in python are unordered collection of unique elements
#Creating a set

prime_numbers = {2, 3, 5, 7, 11}
print(prime_numbers)

#Accessing elements in a set
for number in prime_numbers:
    print(number)

#Adding elements to a set
prime_numbers.add(13)
print(prime_numbers)

#Updating elements in a set
prime_numbers.update([17, 19, 23])
print(prime_numbers)

#Deleting elements from a set using remove()
prime_numbers.remove(17)
print(prime_numbers)

#Deleting elements from a set using discard()
prime_numbers.discard(19)
print(prime_numbers)

#Deleting elements from a set using pop()
prime_numbers.pop()
print(prime_numbers)

#Deleting elements from a set using clear()
prime_numbers.clear()
print(prime_numbers)

#Copying elements in a set using copy()
prime_numbers = {2, 3, 5, 7, 11}
prime_numbers.copy()

#Counting elements in a set using len()
print(len(prime_numbers))

#Checking if an element exists in a set using in
print(2 in prime_numbers)

#Checking if an element exists in a set using not in
print(13 not in prime_numbers)

#Checking if a set is a subset of another set using issubset()
prime_numbers = {2, 3, 5, 7, 11}
numbers = {2, 3, 5}
print(numbers.issubset(prime_numbers))

#Checking if a set is a superset of another set using issuperset()
print(prime_numbers.issuperset(numbers))

#Checking if two sets have common elements using isdisjoint()
even_numbers = {2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))

#Union of two sets using union()
print(numbers.union(prime_numbers))

#Intersection of two sets using intersection()
print(numbers.intersection(prime_numbers))

#Difference of two sets using difference()
print(prime_numbers.difference(numbers))

#Symmetric difference of two sets using symmetric_difference()
print(prime_numbers.symmetric_difference(numbers))

#Copying elements in a set using copy()
prime_numbers = {2, 3, 5, 7, 11}
prime_numbers.copy()
print(prime_numbers)

#Counting elements in a set using len()
print(len(prime_numbers))

#Sorting elements in a set using sorted()
print(sorted(prime_numbers))

#Reversing elements in a set using reversed()
print(reversed(prime_numbers))

#Checking if an element exists in a set using in
print(2 in prime_numbers)
