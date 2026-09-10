# Today's Focus:
# Practicing Python Lists, List Methods, and Tuples.

# 1st Mini Project
# Student Marks Manager

marks = []

marks.append(int(input("Enter marks of Student 1: ")))
marks.append(int(input("Enter marks of Student 2: ")))
marks.append(int(input("Enter marks of Student 3: ")))
marks.append(int(input("Enter marks of Student 4: ")))
marks.append(int(input("Enter marks of Student 5: ")))
marks.append(int(input("Enter marks of Student 6: ")))

print("\nOriginal Marks:")
print(marks)

marks.sort()

print("\nSorted Marks:")
print(marks)

print("\nHighest Marks:", marks[-1])
print("Lowest Marks:", marks[0])

# ------------------------------------------------

# 2nd Mini Project
# Grocery Shopping List

shopping_list = []

shopping_list.append(input("Enter item 1: "))
shopping_list.append(input("Enter item 2: "))
shopping_list.append(input("Enter item 3: "))
shopping_list.append(input("Enter item 4: "))
shopping_list.append(input("Enter item 5: "))

print("\nYour Shopping List:")
print(shopping_list)

remove_item = input("\nEnter an item to remove: ")
shopping_list.remove(remove_item)

print("\nUpdated Shopping List:")
print(shopping_list)

new_item = input("\nEnter a new item: ")
shopping_list.append(new_item)

print("\nFinal Shopping List:")
print(shopping_list)

# ---------------------------------------------------

# 3rd Mini Project
# Tuple Number Analyzer

numbers = (7, 0, 8, 0, 0, 9, 5, 0)

print("Numbers:", numbers)

number = int(input("Enter a number to count: "))

print("Occurrences:", numbers.count(number))

print("Position of 0:", numbers.index(0))

# Purpose:
# These mini projects are designed to apply the concepts learned through simple, practical programs.