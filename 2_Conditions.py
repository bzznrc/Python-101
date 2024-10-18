# %% [markdown]
# # Conditions 🚦
# A condition is a statement that controls the flow of execution depending on some criteria. It is typically used in `if`, `elif`, and `else` statements (as well as `while` loops, which we'll see in Episode 3).
# 
# The condition evaluates to either **True** or **False**, and the code under the condition is executed if the condition is True. If the condition is False, the code is skipped.
# 
# For example, in the following code:
# ```python
# if x > 10:
#     print("x is greater than 10")
# ```
# The condition is `x > 10`. If this condition is True (i.e., if `x` is indeed greater than 10), then `"x is greater than 10"` will be printed. If the condition is False (i.e., `x` is 10 or less), the print statement will be skipped.
# 
# ```python
# if x > 10:
#     print("x is greater than 10")
# else:
#     print("x is smaller than or equal to 10")
# ```
# In this case, if `x` is 10 or less, we'll have the statement in the else block showing.
# 
# <img src="https://imgflip.com/s/meme/Two-Buttons.jpg" width="500" height="300">

# %%
# Examples of conditions

# Example 1: Simple condition
a = 15
b = 7

if a >= b:
    print("A is bigger than B (or equal, I can see you trying to outsmart me)")  # TRUE
else:
    print("A is smaller than B")  # FALSE

# Example 2: Complex condition
a = 2
b = 3
c = 4

if (a != b or c < 3) and (a > 1):  # (True or False) and True => True and True
    print("YES!")
else:
    print("Result is FALSE")

# %% [markdown]
# # Logical Operators ✅❎
# A condition can be True or False based on the result of a logical expression.
# To define one, we use the following operators (more on that [here](https://www.w3schools.com/python/python_operators.asp)):
# 
# ![Comparison Operators](https://drive.google.com/uc?id=1fFVzy-p9CWndNNWnqScwhqFPP5M7V7D3&export=download)
# 
# ![Logical Operators](https://drive.google.com/uc?id=1fujdEPJnM2ISm2jod7zR-xKJ-mWvwrAR&export=download)
# 
# Examples:
# 
# ```python
# if a > 3:
#     # Do something
# 
# if a <= b:
#     # Do something
# 
# if a > 2 and b > 3:
#     # Do something
# 
# if a == 7:
#     # Do something
# ```
# 
# Watch out for the most classic error a programmer might make, which is using `=` instead of `==` for a logical test:
# 
# - `=` is used to **assign** a value to a variable: `best_biscuit = 'Cuor di Mela'`
# - `==` is used to **compare** values in logical tests: `if best_biscuit == 'Cuor di Mela'`

# %% [markdown]
# # Behold! The Table of Truth 🌟
# 
# Is this the best image of a boolean table on the internet? Probably not.
# 
# ![Boolean Table](https://cdn-learn.adafruit.com/assets/assets/000/051/593/medium800/components_and-or-not_tables.png?1520357909)

# %% [markdown]
# # Code Formatting ✂
# Most programming languages like C, C++, and Java use braces `{}` to define a block of code. Python, however, uses indentation.
# 
# A code block (body of a function, loop, etc.) starts with indentation and ends with the first unindented line. The amount of indentation is up to you, but it must be consistent throughout that block.
# 
# This is how to enclose code blocks in C:
# 
# ```c
# if (time >= 12 && time <= 14) {
#     printf("Time for spaghetti! :)");
# } else {
#     printf("Not time for spaghetti :(");
#     printf("Kidding! It's always time for spaghetti :)");
# }
# ```
# 
# And this is how to do it in Python:

# %%
# Example of code blocks with indentation in Python

# Get the current hour
from datetime import datetime
now = datetime.now()
time = now.hour
print(f"The current hour is {time}")

if 12 <= time <= 14:
    print("Time for spaghetti! :)")
else:
    print("Not time for spaghetti :(")
    print("Kidding! It's always time for spaghetti :)")

# %% [markdown]
# # Elif Statements 🔄
# `elif` is shorthand for "else if". We can add as many as we want between an `if` and an `else`, and each one of them has its own condition.
# 
# Python will read all the options starting from the `if`, down through all the `elif`s, and then the `else`. The first of these options that tests `True` gets executed, and everything else in the statement is skipped. The program then resumes from the first line outside the `if`/`else` block.

# %%
biscuit = input("My favourite biscuit is: ")

if biscuit == "Cuor di Mela":
    print("<3")
elif biscuit == "Baiocchi":
    print("That's great!")
elif biscuit == "Gocciole":
    print("Fair")
else:
    print("We're not biscuit pals :(")

print("The program resumes here!")

# %% [markdown]
# # Nested Conditions 🎁
# In the code that gets executed within one branch, we can insert another `if`/`else` statement. In this case, we have *nested* conditions.
# 
# *Inception intensifies.*

# %%
biscuit = input("My favourite biscuit is: ")

if biscuit == "Cuor di Mela":
    really_really_sure = input("Are you REALLY REALLY SURE? ")
    if really_really_sure.lower() in ["yes", "y"]:
        print("<3 <3 <3")
    else:
        print("</3")
elif biscuit == "Baiocchi":
    print("That's great!")
elif biscuit == "Gocciole":
    print("Fair")
else:
    print("We're not biscuit pals :(")

print("The program resumes here!")

# %% [markdown]
# # Libraries and Random! 📚
# Now we'll have a look at **libraries**, and especially at the `random` one.
# 
# A library is a ready-to-use and widely used collection of code that anyone can include in their projects in order not to have to reinvent the wheel every time. Most often, these collections are developed and updated for free by communities of programmers.
# 
# Programmers are very nice people.
# 
# We can access the `random` library with an `import` statement. From then on, we can access its content with dot notation, as if its contents were subfolders within the main `random` folder.
# 
# What we'll use is the `random.randint()` function, which takes a minimum and maximum value as inputs (i.e., within the brackets and comma-separated) and returns a random integer within the boundaries as output (which is a value we can then assign to a variable).

# %%
import random  # 'random' is the library, 'randint()' is the function we'll use

n_min = 1
n_max = 100

# Providing my n_min and n_max variables as the inputs for the randint function
n_ran = random.randint(n_min, n_max)
print("Random nr. 1:", n_ran)

n_ran = random.randint(n_min, n_max)
print("Random nr. 2:", n_ran)

# We can also provide inputs directly, without using variables
print("Random nr. 3:", random.randint(1000, 10000))

# %% [markdown]
# # Baiocchi Slot Machine! 🍪
# 
# And now we have everything we need to build our ~~drinking game!~~
# 
# Ahem... our Baiocchi Slot Machine!

# %%
import random

ran = random.randint(1, 10)
print("Random number:", ran)

if ran == 10:
    print("THREE BAIOCCHIS! 🍪🍪🍪")
elif ran >= 5:
    print("One Baiocco! 🍪")
else:
    print("No Baiocchis :(")

# %% [markdown]
# # Exercise 1 - Guess My Number 🧞
# 
# Write a program that:
# 
# - Generates a random number (between 1 and 10)
# - Asks the user for a guess (between 1 and 10)
# - If the numbers are equal, prints something nice for the user
# - Prints both numbers regardless of their values (this is for checking what's going on)

# %%
# Exercise 1 code here
import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Congratulations! You guessed it!")
else:
    print("Sorry, that's not it.")

print(f"The secret number was {secret_number}, and your guess was {guess}.")

# %% [markdown]
# # Exercise 2 - Risk! 1 Throw / 1 Dice 🚀
# 
# Okay, so we don't know loops yet, so we can't really code a full-fledged Risk! battle, but we can definitely code just one dice throw.
# 
# Simulate the result of one turn where a player attacks with 1 tank and another defends with 1 tank.

# %%
# Exercise 2 code here
import random

attacker_roll = random.randint(1, 6)
defender_roll = random.randint(1, 6)

print(f"Attacker rolls: {attacker_roll}")
print(f"Defender rolls: {defender_roll}")

if attacker_roll > defender_roll:
    print("Attacker wins! Defender loses one unit.")
elif defender_roll >= attacker_roll:
    print("Defender wins! Attacker loses one unit.")

# %% [markdown]
# # Exercise 3 - Guess 3 Times 🥉🥈🥇
# 
# Generate a random number and ask the user to guess if it's even or odd. If they're right, do it again. If they're right, do it again. If they're right, just stop please (and congratulate them).

# %%
# Exercise 3 code here
import random

for attempt in range(1, 4):
    ran = random.randint(1, 10)
    eo = int(input(f"Attempt {attempt}: Is the number Even (0) or Odd (1)? "))
    if ran % 2 == eo:
        print(f"Success! {attempt}")
        if attempt == 3:
            print("Congratulations! You guessed correctly three times!")
            break
    else:
        print("Incorrect guess.")
        print("Good luck next time!")
        break
