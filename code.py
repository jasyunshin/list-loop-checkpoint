# Name: Jason Shin
# Period: AM
# ============================================================
# Python Skills Check — LISTS & LOOPS
# CHALLENGE VERSION — 40 TASKS
# ============================================================
# DIRECTIONS:
# - Create a repository, clone it, and add this file.
# - Complete each task UNDER its directions.
# - Do not delete the directions.
# - Use ONLY concepts learned in class, except for 'in' and 'not in'.
# You must research these two new operators independently in Section 5.
# - Use the EXACT variable and function names provided.
# - The entire file must run without errors.
# - Do not hard-code results Python should calculate.
# - Unless a task says otherwise, do NOT use sum(), min(), max(),
# sorted(), sort(), list comprehensions, sets, or dictionaries.
# - For functions, RETURN values when instructed; do not just print.
# - Test edge cases and change the starting values to check your logic.
# - Tasks that ask for input() may be tested individually.
# ============================================================
# SECTION 1 — LIST FUNDAMENTALS (TASKS 1–6)
# ============================================================
# TASK 1:
# Create a list named scores containing 85, 92, 78, 96, 88.
# Print the entire list and its length using len().

scores = [85, 92, 78, 96, 88]
print(scores)
print(len(scores))

# TASK 2:
# Using scores from Task 1, print the FIRST, THIRD, and LAST
# elements on separate lines. Use indexes, not hard-coded values.

print(scores[0])
print(scores[2])
print(scores[4])

# TASK 3:
# Change the third element of scores to 100.
# Print the updated list. Do not create a replacement list.
scores[2] = 100
print(scores)

# TASK 4:
# Create games = ["Minecraft", "Roblox", "Fortnite"].
# Append "Valorant" and insert "Rocket League" at index 1.
# Print games. Check the order carefully.

games = ["Minecraft", "Roblox", "Fortnite"]
games.append("Valorant")
games.insert(1, "Rocket League")
print(games)

# TASK 5:
# Using games from Task 4, remove "Roblox" with remove().
# Then pop the FIRST item into a variable named removed_game.
# Print removed_game and the remaining games list.

games.remove("Roblox")
removed_game = games.pop(0)
print(removed_game)
print(games)


# TASK 6:
# Create colors = ["red", "blue", "green", "yellow", "purple"].
# Store the index of "green" in green_index using index().
# Print green_index. Then replace "yellow" with "orange".
# Print the new list.

colors = ["red", "blue", "green", "yellow", "purple"]
green_index = colors.index("green")
print(green_index)
colors[3] = "orange"
print(colors)

# ============================================================
# SECTION 2 — FOR LOOPS & RANGE (TASKS 7–12)
# ============================================================
# TASK 7:
# Use a for loop with range() to print numbers 1 through 20,
# INCLUDING 20. Do not manually print the numbers.

for i in range(1, 21):
    print(i)
# TASK 8:
# Use a for loop with range() to print 30, 27, 24, ... 0.
# IMPORTANT: The zero must be included.

for a in range(30, -1, -3):
    print(a)
# TASK 9:
# Use a for loop to print all EVEN numbers from 1 to 50.
# You MUST use an if statement and the % operator inside the loop.

for a in range(1, 51):
    if a % 2 == 0:
        print(a)
# TASK 10:
# Create number = 7.
# Print its multiplication table from 1 through 12 using a for loop.
# Example line: 7 x 3 = 21
# Your code must also work if number changes.
number = 7

for multiplier in range(1, 13):
    print(number, "x", multiplier, "=", number * multiplier)

# TASK 11:
# Create students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"].
# Use a for loop to print "Student: " followed by each name.
# Do NOT write five separate print statements.

students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
for student in students:
    print("Student:", student)

# TASK 12:
# Using students, print a NUMBERED roster:
# 1. Alex
# 2. Jordan
# ...
# 5. Casey
# Use range(len(students)) OR enumerate().

for index in range(len(students)):
    print(str(index + 1) + ".", students[index])

# ============================================================
# SECTION 3 — WHILE LOOPS & VALIDATION (TASKS 13–18)
# ============================================================
# TASK 13:
# Create countdown = 10.
# Use a while loop to print from countdown down to 0.
# Then print "Blast off!". Avoid an infinite loop.

countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("Blast off!")
# TASK 14:
# Create password = "Python123".
# Keep asking the user for a password until it matches.
# Print "Access granted" exactly once after a correct entry.

password = "Python123"
user_input = ""
while user_input != password:
    user_input = input("Enter password: ")
print("Access granted")
# TASK 15:
# Ask the user for an integer between 1 and 10 INCLUSIVE.
# Keep asking while the value is invalid.
# After a valid entry, print "Valid number".
# Test 0, 1, 10, and 11.
user_input = int(input("Enter an integer between 1 and 10: "))
while user_input < 1 or user_input > 10:
    user_input = int(input("Invalid. Enter an integer between 1 and 10: "))
print("Valid number")

# TASK 16:
# Create total = 0.
# Repeatedly ask for an integer. Add each nonzero entry to total.
# Stop when the user enters 0, then print total.
# Example inputs: 5, 8, -2, 0 -> Total: 11.

total = 0
number = int(input("Enter an integer: "))

while number != 0:
    total += number
    number = int(input("Enter an integer: "))

print("Total:", total)
# TASK 17:
# Create secret = "robot" and attempts = 3.
# Ask the user to guess secret, allowing AT MOST 3 guesses.
# Print "Correct" if guessed in time; otherwise "Out of attempts".
# Make sure a correct guess does NOT print both messages.

secret = "robot"
attempts = 3
guess = ""

while attempts > 0 and guess != secret:
    guess = input("Guess the secret: ")
    attempts -= 1

if guess == secret:
    print("Correct")
else:
    print("Out of attempts")


# TASK 18:
# Make a while-loop menu:
# 1. Say Hello
# 2. Say Goodbye
# 3. Exit
# Repeat until the user enters 3. Handle invalid choices.
# Print "Goodbye" only when option 2 is selected.

choice = ""

while choice != "3":
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice != "3":
        print("Invalid choice")


# ============================================================
# SECTION 4 — PROCESSING LISTS WITH LOOPS (TASKS 19–24)
# ============================================================

# TASK 19:
# Create numbers = [4, 8, 15, 16, 23, 42].
# Use a for loop to calculate and print their total.
# Do NOT use sum().

numbers = [4, 8, 15, 16, 23, 42]
total = 0

for number in numbers:
    total += number

print("Total:", total)


# TASK 20:
# Create grades = [90, 85, 78, 92, 88].
# Use a loop and len() to calculate the average.
# Print the average. Do NOT use sum().

grades = [90, 85, 78, 92, 88]
total = 0

for grade in grades:
    total += grade

average = total / len(grades)
print("Average:", average)


# TASK 21:
# Create numbers = [3, 8, 12, 7, 15, 20, 24, 9].
# Use ONE loop to count even and odd values separately.
# Print "Even: [count]" and "Odd: [count]".

numbers = [3, 8, 12, 7, 15, 20, 24, 9]
even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)


# TASK 22:
# Create numbers = [-14, -67, -23, -89, -45].
# Use a loop to find and print the HIGHEST number.
# Do NOT use max() or sorting.
# IMPORTANT: Starting your answer at 0 gives a wrong result.

numbers = [-14, -67, -23, -89, -45]
highest = numbers[0]

for number in numbers:
    if number > highest:
        highest = number

print("Highest:", highest)


# TASK 23:
# Create numbers = [14, 67, 23, 89, 45, 12].
# Use a loop to find and print the LOWEST number.
# Do NOT use min() or sorting.
# Your logic must also work with all-negative numbers.

numbers = [14, 67, 23, 89, 45, 12]
lowest = numbers[0]

for number in numbers:
    if number < lowest:
        lowest = number

print("Lowest:", lowest)


# TASK 24:
# Create numbers = [5, 2, 5, 8, 5, 3, 2, 5].
# Create target = 5.
# Use a loop to count how often target appears; print the count.
# Do NOT use count(). It must work if target changes.

numbers = [5, 2, 5, 8, 5, 3, 2, 5]
target = 5
matches = 0

for number in numbers:
    if number == target:
        matches += 1

print("Count:", matches)


# ============================================================
# SECTION 5 — IN / NOT IN (TASKS 25–30)
# ============================================================

# INDEPENDENT RESEARCH REQUIRED:
# We have NOT covered 'in' and 'not in' in class. Before starting
# Tasks 25–30, research both operators on your own using reliable
# Python learning resources or the official Python documentation.
# Learn what each operator does, how it works with lists, and how
# to use it inside if statements and while loops.
# Write a short comment in your code explaining the difference
# between 'in' and 'not in' in your own words.
# The examples below are starting hints, NOT a substitute for research.
#
# NEW CONCEPT:
# 'in' checks whether a value is in a list.
# Example: "apple" in ["apple", "banana"] evaluates to True.
# 'not in' checks whether a value is missing.
# Example: "grape" not in ["apple", "banana"] evaluates to True.
# These expressions are useful in if statements and while loops.

# Research source:
# https://docs.python.org/3/reference/expressions.html#membership-test-operations
# "in" checks if something is there; "not in" checks if it is missing.


# TASK 25:
# Create foods = ["pizza", "burger", "tacos", "sushi", "pasta"].
# Ask the user to enter a food.
# Use 'in' to print "Available" or "Not available".
# Do NOT use index() to search.

foods = ["pizza", "burger", "tacos", "sushi", "pasta"]
food = input("Enter a food: ")

if food in foods:
    print("Available")
else:
    print("Not available")


# TASK 26:
# Create supplies = ["pencil", "notebook", "eraser", "backpack"].
# Ask the user for an item.
# Use 'not in' to print "Need to buy" if it is missing,
# otherwise print "Already have it".

supplies = ["pencil", "notebook", "eraser", "backpack"]
item = input("Enter an item: ")

if item not in supplies:
    print("Need to buy")
else:
    print("Already have it")


# TASK 27:
# Create usernames = ["alex123", "gamer99", "pythonpro"].
# Ask the user to enter a new username.
# If it is already in the list, print "Username taken".
# Otherwise append it and print the updated list.
# Do not allow duplicates.

usernames = ["alex123", "gamer99", "pythonpro"]
username = input("Enter a new username: ")

if username in usernames:
    print("Username taken")
else:
    usernames.append(username)
    print(usernames)


# TASK 28:
# Modify the idea from Task 27 using a NEW list named accounts.
# Start with accounts = ["admin", "guest"].
# Use a while loop to keep asking until the entered name
# is NOT in accounts. Append the accepted name and print accounts.
# REQUIREMENT: Use 'not in' in your solution.

accounts = ["admin", "guest"]
accepted = False

while accepted == False:
    name = input("Enter a new account name: ")

    if name not in accounts:
        accounts.append(name)
        accepted = True
    else:
        print("Username taken")

print(accounts)


# TASK 29:
# Create secret_words = ["dragon", "robot", "python", "galaxy"].
# Keep asking the user for a word UNTIL it is in secret_words.
# Count and print the number of guesses made.
# A correct first guess should count as 1.

secret_words = ["dragon", "robot", "python", "galaxy"]
guesses = 1
word = input("Guess a word: ")

while word not in secret_words:
    word = input("Try again: ")
    guesses += 1

print("Guesses:", guesses)


# TASK 30:
# Create guests = [].
# Ask the user to enter EXACTLY FIVE UNIQUE guest names.
# If a name is already in guests, reject it and ask again.
# Use a while loop, 'in' or 'not in', and append().
# Print the finished list and its length.

guests = []

while len(guests) < 5:
    name = input("Enter a guest name: ")

    if name in guests:
        print("That guest is already on the list")
    else:
        guests.append(name)

print(guests)
print("Number of guests:", len(guests))


# ============================================================
# SECTION 6 — LISTS + FUNCTIONS (TASKS 31–35)
# ============================================================

# TASK 31:
# Create a function named count_positive(numbers).
# RETURN how many elements are greater than 0.
# Do NOT use count().
# Test: count_positive([-2, 0, 4, 9, -1]) -> 2

def count_positive(numbers):
    positives = 0

    for number in numbers:
        if number > 0:
            positives += 1

    return positives


print(count_positive([-2, 0, 4, 9, -1]))


# TASK 32:
# Create a function named find_item(items, target).
# RETURN the index of the FIRST matching item, or -1 if missing.
# Do NOT use index().
# Test: find_item(["cat", "dog", "cat"], "cat") -> 0
# Test: find_item(["cat", "dog"], "fish") -> -1

def find_item(items, target):
    for index in range(len(items)):
        if items[index] == target:
            return index

    return -1


print(find_item(["cat", "dog", "cat"], "cat"))
print(find_item(["cat", "dog"], "fish"))


# TASK 33:
# Create a function named unique_items(items).
# RETURN a NEW list without duplicate values, preserving first
# appearance order. REQUIREMENT: Use 'not in'.
# Test: unique_items([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]

def unique_items(items):
    unique = []

    for item in items:
        if item not in unique:
            unique.append(item)

    return unique


print(unique_items([1, 2, 2, 3, 1, 4]))


# TASK 34:
# Create a function named common_items(list1, list2).
# RETURN a NEW list of values found in BOTH lists.
# Include each matching value only once, in list1's order.
# REQUIREMENT: Use both 'in' and 'not in'.
# Test: common_items([1, 2, 3, 3], [3, 4, 1]) -> [1, 3]

def common_items(list1, list2):
    common = []

    for item in list1:
        if item in list2:
            if item not in common:
                common.append(item)

    return common


print(common_items([1, 2, 3, 3], [3, 4, 1]))


# TASK 35:
# Create a function named reverse_list(items).
# RETURN a NEW list in reverse order, without changing items.
# Do NOT use reverse(), reversed(), or [::-1].
# Test: reverse_list([10, 20, 30]) -> [30, 20, 10]

def reverse_list(items):
    result = []

    for index in range(len(items) - 1, -1, -1):
        result.append(items[index])

    return result


print(reverse_list([10, 20, 30]))


# ============================================================
# SECTION 7 — DEBUGGING (TASKS 36–37)
# ============================================================

# TASK 36:
# Fix this code so it prints 1, 2, 3, 4, 5 exactly once each.
# Explain in a comment what was wrong.
#
# number = 1
# while number <= 5:
# print(number)
#
# Do NOT replace the while loop with a for loop.

# The print needed indentation, and number needed to increase.
number = 1

while number <= 5:
    print(number)
    number += 1


# TASK 37:
# Fix this code so it removes ALL 4s without skipping any.
# Explain in a comment why the original approach can fail.
#
# values = [4, 4, 7, 4, 9]
# for value in values:
# if value == 4:
# values.remove(value)
# print(values)
#
# Expected: [7, 9]
# HINT: A while loop and 'in' can help.

# Removing items during a for loop shifts indexes and can skip items.
values = [4, 4, 7, 4, 9]

while 4 in values:
    values.remove(4)

print(values)


# ============================================================
# FINAL BOSS CHALLENGES (TASKS 38–40)
# ============================================================

# TASK 38 — SHOPPING LIST MANAGER:
# Build a menu-driven program with:
# 1. Add item
# 2. Remove item
# 3. View numbered items
# 4. Search for item
# 5. Exit
# Start with shopping_list = [].
# REQUIREMENTS:
# - Use a while loop for the menu and a for loop to display items.
# - Use 'in' to prevent duplicates and 'not in' to reject missing items.
# - Handle an empty list and invalid menu selections.
# - Keep running until the user chooses Exit.

shopping_list = []
choice = ""

while choice != "5":
    print("1. Add item")
    print("2. Remove item")
    print("3. View numbered items")
    print("4. Search for item")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter an item to add: ")

        if item in shopping_list:
            print("Item already on the list")
        else:
            shopping_list.append(item)
            print("Item added")

    elif choice == "2":
        item = input("Enter an item to remove: ")

        if item not in shopping_list:
            print("Item not found")
        else:
            shopping_list.remove(item)
            print("Item removed")

    elif choice == "3":
        if len(shopping_list) == 0:
            print("Your list is empty")
        else:
            for index in range(len(shopping_list)):
                print(str(index + 1) + ".", shopping_list[index])

    elif choice == "4":
        item = input("Enter an item to search for: ")

        if item in shopping_list:
            print("Item found")
        else:
            print("Item not found")

    elif choice != "5":
        print("Invalid choice")


# TASK 39 — GRADE ANALYZER:
# Create a function named analyze_grades(grades).
# RETURN a list containing, IN THIS ORDER:
# [highest_grade, lowest_grade, average_grade, passing_count, failing_count]
# Passing means 70 or higher.
# Do NOT use sum(), min(), max(), or sorting.
# For an empty list, RETURN [].
# Test: analyze_grades([95, 82, 67, 74, 58])
# Expected: [95, 58, 75.2, 3, 2]
# Test with a single grade and all-negative values too.

def analyze_grades(grades):
    if len(grades) == 0:
        return []

    highest = grades[0]
    lowest = grades[0]
    total = 0
    passing = 0
    failing = 0

    for grade in grades:
        total += grade

        if grade > highest:
            highest = grade

        if grade < lowest:
            lowest = grade

        if grade >= 70:
            passing += 1
        else:
            failing += 1

    average = total / len(grades)

    return [highest, lowest, average, passing, failing]


print(analyze_grades([95, 82, 67, 74, 58]))
print(analyze_grades([85]))
print(analyze_grades([-10, -20, -30]))
print(analyze_grades([]))


# TASK 40 — STUDENT ATTENDANCE SYSTEM:
# Start with:
# students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
# present = []
# absent = []
# For EACH student, ask whether they are Present (P) or Absent (A).
# REQUIREMENTS:
# - Use a for loop to process the student list.
# - Use a while loop to reject anything other than P or A.
# - Prevent duplicate attendance records using 'in' / 'not in'.
# - Print numbered present and absent lists.
# - Print the number present, number absent, and attendance percentage.
# - Print "Perfect Attendance!" if everyone is present.
# - Create attendance_percentage(present, students) that RETURNS
# the percentage; if students is empty, RETURN 0.
# - Test with all present, all absent, and a mixture.

def attendance_percentage(present, students):
    if len(students) == 0:
        return 0

    return len(present) / len(students) * 100


students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
present = []
absent = []

for student in students:
    if student not in present:
        if student not in absent:
            status = input(student + " - Present (P) or Absent (A): ")

            while status not in ["P", "A"]:
                status = input("Please enter P or A: ")

            if status == "P":
                present.append(student)
            else:
                absent.append(student)

print("Present:")
if len(present) == 0:
    print("None")

for index in range(len(present)):
    print(str(index + 1) + ".", present[index])

print("Absent:")
if len(absent) == 0:
    print("None")

for index in range(len(absent)):
    print(str(index + 1) + ".", absent[index])

print("Number present:", len(present))
print("Number absent:", len(absent))
print("Attendance percentage:", attendance_percentage(present, students))

if len(present) == len(students):
    print("Perfect Attendance!")

# Percentage tests for all present, all absent, and mixed attendance.
print(attendance_percentage(students, students))
print(attendance_percentage([], students))
print(attendance_percentage(["Alex", "Taylor"], students))

# Test the full program by running it three times:
# Enter P for everyone, A for everyone, then a mixture of P and A.


# ============================================================
# END OF CHECKPOINT — REVIEW YOUR WORK BEFORE PUSHING
# ============================================================