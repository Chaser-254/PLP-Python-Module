#  for loop in python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#The for loop does not require an indexing variable to set beforehand.

five_steps = range(5)
for step in five_steps:
    print(step)
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

count = 1
while count < 6:
    print(count)
    count += 1

for number in range(1, 6):
    if number == 3:
        print("Number 3 is skipped")
        break
    elif number == 5:
        print("Number 5 is skipped")
        continue
    print(number)
#The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.
