# %% [markdown]
# # Lists 📋
# 
# You may have wondered what happens when, instead of having just a few values which you can store in just a few variables, you have lots of values that you have to put somewhere. Maybe you don't know how many in advance. Maybe you have to sort them. Maybe at some point you'll delete or add some.
# 
# ~~There's an app for that.~~ You'll need **lists** for that.
# 
# **Quick list of facts about lists:**
# - Lists are a collection of values.
# - A list is comprised of elements within square brackets, separated by commas.
# - Each element in the list is identified by its **position** and holds a **value**.
# - You can get to an element's value by specifying its position.
# 
# Also, remember every single time you had to count something, how you always start with 1? It makes sense, right? Forget that, we're counting from 0 now (programmers are weird people).

# %%
# Creating a list of numbers
my_list = [4, 5, 7, 9, 24]

# Let's print the whole list
print("Whole list:", my_list)

# Print the 3rd element in my_list (remember, it starts from 0)
print("3rd element (my_list[2]):", my_list[2])

# Creating a list of strings
food_list = ["sushi", "pizza", "burger"]

# Print the whole list
print("Whole list:", food_list)

# Print the 1st element in food_list
print("1st element (food_list[0]):", food_list[0])

# We can combine lists
some_nice_movies = ['Vertigo', 'Birdman', 'Inception']
some_other_nice_movies = ['Moonrise Kingdom', 'Hot Fuzz', 'Inside Out']

lots_of_nice_movies = some_nice_movies + some_other_nice_movies

print("Lots of nice movies:", lots_of_nice_movies)

# Checking if an element is in the list
print("Is 'Titanic' in the list?", "Titanic" in lots_of_nice_movies)
print("Is 'Inception' in the list?", "Inception" in lots_of_nice_movies)

# Using 'in' operator with conditions
if "Titanic" not in lots_of_nice_movies:
    print("Giusto")  # Correct in Italian

if "Titanic" in lots_of_nice_movies:
    print("I beg to differ")

# %% [markdown]
# # Remove & Append 🗑 📌
# 
# **`list.remove(value)`**
# 
# The `remove()` method removes the first occurrence of the element with the specified value.
# 
# **`list.append(value)`**
# 
# The `append()` method adds an element to the end of the list.

# %%
TMNT_list = ["Leonardo", "Michelangelo", "Donatello", "Bob"]

# Printing the original list
print("TMNT 1:", TMNT_list)

# Removing the wrong element and printing
TMNT_list.remove("Bob")
print("TMNT 2:", TMNT_list)

# Adding the correct name and printing
TMNT_list.append("Raffaello")
print("TMNT 3:", TMNT_list)

# %% [markdown]
# # For Loops ➰
# 
# So we learned loops already, focusing on *while* loops. Now we're looking at [**for** loops](https://www.w3schools.com/python/python_for_loops.asp), which do the same thing but are much friendlier to work with. They're also best buddies with *lists*. 🤜🤛
# 
# A `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# 
# The examples below show the same thing written with an old-fashioned `while` statement and then a `for` statement:

# %%
TMNT_list = ["Leonardo", "Michelangelo", "Donatello", "Raffaello"]

# Using a while loop
i = 0  # Counter
while i < len(TMNT_list):
    print("[WHILE] Hey, I'm", TMNT_list[i])
    i += 1  # Increment the counter

# Using a for loop
for ninja in TMNT_list:
    print("[FOR] Hey, I'm", ninja)

# Nested loops example
adj = ["Mighty", "Cyber", "Below-Average"]
noun = ["Plumber", "Corgi", "Pasta"]

for a in adj:
    for n in noun:
        print(a, n)  # This will print all 9 combinations

# %% [markdown]
# # List Shuffle 🔀
# 
# Do you remember how amazing the `random` package was?
# 
# Turns out it can shuffle your lists as well! Yippee!

# %%
import random

teletubbies = ['Tinky Winky', 'Dipsy', 'Laa-Laa', 'Po']

print("STRAIGHT")
for tlt in teletubbies:
    print(tlt)

# Now let's shuffle this
random.shuffle(teletubbies)  # This alters the list directly

print("\nSHUFFLED")
for tlt in teletubbies:
    print(tlt)

# %% [markdown]
# # Something Actually Useful
# 
# (for a change)
# 
# This is how we read all the files in a folder. You can see the locations get stored in a list. Of course, it couldn't work with variables because we don't know how many they are before opening the folder.
# 
# Once we have all the locations, we can open them and save them in a DataFrame variable (which is kind of a complex data structure that you can think of as a table, with columns and rows).

# %%
import pandas as pd

# This is where the files are
dir_path = "/FileStore/py101/files_examples"

# We get all their links and put them into a list
file_paths = [file.path for file in dbutils.fs.ls(dir_path)]

data_frames = []  # We create an empty list
for file_path in file_paths:
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
        data_frames.append(df)
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
        data_frames.append(df)

# Do something with the list of data frames

# %% [markdown]
# # Everything Else 🌌
# 
# Ok, so we've focused on lists and the for loops you can do with them. There are a few other ways to store multiple items into a single structure. Let's go quickly through them:
# 
# - **[List](https://www.w3schools.com/python/python_lists.asp)** is a collection which is **ordered** and **changeable**. Allows duplicate members.
# - **[Tuple](https://www.w3schools.com/python/python_tuples.asp)** is a collection which is **ordered** and **unchangeable**. Allows duplicate members.
# - **[Set](https://www.w3schools.com/python/python_sets.asp)** is a collection which is **unordered** and **unindexed**. No duplicate members.
# - **[Dictionary](https://www.w3schools.com/python/python_dictionaries.asp)** is a collection which is **unordered**, **changeable**, and **indexed**. No duplicate members.
# 
# ### What do you mean, indexed?
# 
# "Indexed" means that the elements in the structure are assigned a certain position or index, and you can access the element directly using that index.
# 
# In a dictionary or a set, the elements are not indexed numerically like `dict[0]` or `set[0]`. In a dictionary, you access values using their corresponding keys, and in a set, you can only check if a value exists or iterate through the values, but you can't access a specific item by an index.

# %%
# Lists
thislist = ["apple", "banana", "banana"]
print("List:", thislist)

# Tuples
thistuple = ("apple", "banana", "banana")
print("Tuple:", thistuple)

# Sets
thisset = {"apple", "banana", "banana"}
print("Set:", thisset)  # Note that duplicates are removed

# %% [markdown]
# # Buon Compleanno! 🎂
# 
# Ok, this is a HUGE Nerd Alert.
# 
# Let's pretend you have a big room and lots of random people. You make them get in one by one. How long until you get two people with the same birthday in the room?
# 
# The problem is quite famous, and we're now solving it with a Monte Carlo approach (which is a fancy way of saying, let's do an insane amount of trials and see how the results look like on average).

# %%
import random
import matplotlib.pyplot as plt

trials = 10000
results = []

# Run experiments
for _ in range(trials):
    people = []
    people_set = set()
    while len(people) == len(people_set):
        person = random.randint(1, 365)
        people.append(person)
        people_set.add(person)
    results.append(len(people))

# Print the average number of people in the room
average = sum(results) / len(results)
print('Average number of people in the room:', round(average, 4))

# Plot the results
plt.hist(results, bins=range(1, max(results)+1), edgecolor='black')
plt.xlabel('Number of people')
plt.ylabel('Frequency')
plt.title('Birthday Paradox Simulation')
plt.show()

# %% [markdown]
# # Dictionaries 📖
# 
# Let's go into a bit more detail with **[dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)**:
# 
# - Dictionaries are collections of key/value pairs.
# - You can get to a value by specifying its key.
# - Both keys and values can be strings (text) or numbers.
# - They are super useful for lots of things where the time performance in retrieving your values is important.

# %%
# Example of a dictionary - The key is a string, the value is a number
my_dict = {"Baiocchi": 100, "Tarallucci": 25, "Gocciole": 80}

# Print the value for "Tarallucci"
print("Tarallucci:", my_dict["Tarallucci"])

# Another dictionary - Both keys and values are strings
fav_food = {
    "Italy": "pizza",
    "Japan": "sushi",
    "USA": "burger"
}

# Print the value for "USA"
print("Favorite food in USA:", fav_food["USA"])

# %% [markdown]
# # Exercise 1 - Kitchen Management 👩‍🍳👨‍🍳🍳
# 
# Let's write a bit of logic to manage the ingredients in a kitchen.
# As this is a bit of a long one, we'll split it into three parts.
# 
# ## Part 1
# 
# - We'll ask the user to provide us with the ingredients, one by one.
# - We don't know how many ingredients we'll have (so we'll use a `while` loop).

# %%
ingredients = []

while True:
    response = input("Wanna give me an ingredient? (yes/no) ")
    if response.lower() == "no":
        break
    ingredient = input("What's the ingredient? ")
    ingredients.append(ingredient)

print("The list looks like this:", ingredients)

# Adding some default ingredients
ingredients.extend(["oranges", "pears"])

# %% [markdown]
# ## Part 2
# 
# - Let's now ask the user which ingredients they used, one at a time.
# - Let's remove that ingredient from the list (if it's there).
# - At the end, let's print the updated list.

# %%
while True:
    response = input("Wanna remove an ingredient? (yes/no) ")
    if response.lower() == "no":
        break
    rem = input("What's the ingredient to remove? ")
    if rem in ingredients:
        ingredients.remove(rem)
        print(f"Removed {rem}.")
    else:
        print(f"{rem} is not in the list.")

print("The updated list is:", ingredients)

# %% [markdown]
# ## Part 3
# 
# The user has now gone to do some grocery shopping.
# 
# - Let's ask them which new ingredients they bought, one at a time.
# - Let's check if that ingredient was present already. If it wasn't, let's add it.

# %%
while True:
    response = input("Did you buy a new ingredient? (yes/no) ")
    if response.lower() == "no":
        break
    new_ing = input("What's the new ingredient? ")
    if new_ing in ingredients:
        print(f"{new_ing} is already in the list.")
    else:
        ingredients.append(new_ing)
        print(f"Added {new_ing} to the list.")

print("The final list is:", ingredients)

# %% [markdown]
# # Exercise 2 - Better Kitchen Management 👩‍🍳👨‍🍳🍳
# 
# Let's rewrite the previous three code blocks, but with a **dictionary** instead of a *list*.
# 
# The dictionary will have the ingredients as keys and the quantities as values. This way, you can have more than one of each.
# 
# This sounds like a better idea.

# %%
inventory = {}

# Part 1: Initialize ingredients
while True:
    response = input("Wanna give me an ingredient? (yes/no) ")
    if response.lower() == "no":
        break
    ingredient = input("What's the ingredient? ")
    quantity = int(input(f"How many {ingredient}s do you have? "))
    inventory[ingredient] = inventory.get(ingredient, 0) + quantity

print("Current inventory:", inventory)

# Part 2: Use ingredients
while True:
    response = input("Did you use an ingredient? (yes/no) ")
    if response.lower() == "no":
        break
    used_ing = input("What's the ingredient you used? ")
    if used_ing in inventory and inventory[used_ing] > 0:
        inventory[used_ing] -= 1
        print(f"Used one {used_ing}. Remaining: {inventory[used_ing]}")
        if inventory[used_ing] == 0:
            del inventory[used_ing]
            print(f"No more {used_ing}s left.")
    else:
        print(f"You don't have any {used_ing}.")

print("Updated inventory:", inventory)

# Part 3: Restock ingredients
while True:
    response = input("Did you buy a new ingredient? (yes/no) ")
    if response.lower() == "no":
        break
    new_ing = input("What's the new ingredient? ")
    quantity = int(input(f"How many {new_ing}s did you buy? "))
    inventory[new_ing] = inventory.get(new_ing, 0) + quantity
    print(f"Added {quantity} {new_ing}(s) to the inventory.")

print("Final inventory:", inventory)
