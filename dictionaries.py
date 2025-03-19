#Python dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key-value pair. Dictionaries are optimized to retrieve values when the key is known.
# empty dictionary
my_dict = {}
#create a dictionary
capital_cities = {
    "India": "New Delhi",
    "USA": "Washington DC",
    "UK": "London",
    "France": "Paris"
}
print(capital_cities)

#Accessing elements in a dictionary
print(capital_cities["India"])
print(capital_cities["USA"])

#Adding elements to a dictionary
capital_cities["Germany"] = "Berlin"
print(capital_cities)

#Updating elements in a dictionary
capital_cities["India"] = "Mumbai"
print(capital_cities)

#Deleting elements from a dictionary using del()
del capital_cities["India"]
print(capital_cities)

#Deleting elements from a dictionary using pop()
capital_cities.pop("USA")
print(capital_cities)

#Deleting elements from a dictionary using clear()
capital_cities.clear()
print(capital_cities)

#Copying elements in a dictionary using copy()
capital_cities = {
    "India": "New Delhi",
    "USA": "Washington DC",
    "UK": "London",
    "France": "Paris"
}
capital_cities.copy()
print(capital_cities)

#Counting elements in a dictionary using len()
print(len(capital_cities))

#Sorting elements in a dictionary using sorted()
print(sorted(capital_cities))

#Reversing elements in a dictionary using reversed()
print(reversed(capital_cities))

#Checking if a key exists in a dictionary using in
print("India" in capital_cities)
