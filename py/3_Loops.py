# %% [markdown]
# # Loops ➰
# *A Loop is a construct used to repeat parts of code until a condition becomes false.*
# 
# **Example:**
# 
# **Until** I get what this means, I'll keep reading this sentence.
# 
# Now, a crucial point about loops (written via *while* statements) is that in order for the program to be able to get *out of a loop*, the variables used in the condition need to be changed within the loop. If this doesn't happen, the condition result will always be the same and the loop won't ever end.
# 
# 🤯
# 
# Let's see an example:

# %%
# Let's say I'm building an annoying machine that gives out the change with 10c coins only
cost = float(input("How much does this cost? "))
paid = float(input("How much did you pay? "))

# Calculating the change we owe
change = paid - cost

# This loop will keep executing as long as the change is > 0
while change > 0:
    print("Here's your 10c")
    # It is crucial that the change value is updated within the loop.
    # So at every new loop, the change value will decrease
    change = round(change - 0.10, 2)  # The round() is to handle floating-point arithmetic
    # We're also printing out the value at each step to better visualize what's going on
    print("Remaining change:", change)

print("Got out of the loop!")

# %% [markdown]
# Like we saw with the `if`, the `while` loop also gets executed if a logical test equals `True`.
# Actually, one might say that a `while` is just an `if` that keeps repeating until the condition stops being `True`.
# 
# All the logical operators we saw for `if` still apply to `while`, as well as the point about the code needing to be properly indented. The code that will get repeated by the `while` is only the indented one.
# 
# # A Few Examples 👨‍💻
# 
# ## Known Number of Loops ❗
# One common kind of loop is the one in which you have to execute the code a predetermined number of times. In the example below, the user will give me a number, and we'll list all the numbers leading up to that one.
# 
# Notice the "`<=`" used in the `while` condition (as opposed to a "`<`"). This way we'll also print the very last number.
# 
# Yes, you could put a very big number there. No, you don't really want to see what happens.

# %%
# This is the number we want to get to
num_max = int(input("What's the max number? "))
# This is the number we're starting from. It's now 1 but will increase at every loop
# This is also called a "counter" variable, because—you guessed it—it counts
num = 1

# We keep going until our counter reaches our max
while num <= num_max:
    print(num)  # Print the current counter value
    num = num + 1  # Increase the counter by 1

# If we're here (which is out of the loop), it means our counter got to the max
print("I got to", num_max, "!")

# %% [markdown]
# ## Unknown Number of Loops ❓
# Another kind of loop is one in which we keep asking the user for an input, and every time we check it against a value that we have already. Note that this time around we don't have a counter, and we're not able to predict how long the loop will run beforehand. It really depends on how good the biscuit tastes of the user are.
# 
# This is also roughly what happens under the hood when you input a password somewhere (there's also a bit of cryptography going on).
# 
# We now ask once for the input outside the loop in order to start it, but then it's crucial that we keep asking it inside the loop as well, for the user to have a chance to tell us that Cuor di Mela are actually the best biscuits.

# %%
answer = input("What's the best biscuit? ")

while answer != "Cuor di Mela":
    answer = input("Not sure I heard that correctly? ")

print("<3")

# %% [markdown]
# This one is kind of a fancier way to write it. Basically, we don't start with a question outside of the loop but we ask the question within the loop condition. When it executes, the `input()` goes through, stopping the execution for the user to input the value, then that value gets compared to the `"Gocciole"` string on the fly.
# 
# In this case, we don't really need to do anything *inside* the loop, so we have a special `pass` command that basically does nothing. If we're outside of the loop, it means that the check returned `True` at some point, then we can cheer.
# 
# This is kinda advanced and I won't lie, I added this mainly for flexing.

# %%
while input("What's the best biscuit? ") != "Gocciole":
    pass

print("<3")

# %% [markdown]
# # Exercise 1 - Ultimate Question ✨
# Keep asking the user for the Answer to the Ultimate Question of Life, the Universe, and Everything.
# 
# When they hit `42`, cheer them.

# %%
# Exercise 1
answer = ""
while answer != "42":
    answer = input("What is the Answer to the Ultimate Question of Life, the Universe, and Everything? ")

print("Congratulations! You've found the answer!")

# %% [markdown]
# # Exercise 2 - Randos 🔢
# Ask the user how many random numbers they want. Also ask them the min and max these numbers need to be within.
# 
# Give them the numbers.

# %%
# Exercise 2
import random

count = int(input("How many random numbers do you want? "))
n_min = int(input("Minimum value: "))
n_max = int(input("Maximum value: "))

print("Here are your random numbers:")

i = 0
while i < count:
    rand_num = random.randint(n_min, n_max)
    print(rand_num)
    i += 1

# %% [markdown]
# # Da Bomb 💣
# Coding is not only about writing code, it's also about figuring out what's written in someone else's.
# 
# Let's try to figure out what goes on in this code:
# - Check the variables defined at the beginning
#   - What's that `win = False` one, you ask? That's a boolean variable (can be either `True` or `False`) and it's initialized as `False`.
# - Focus on the logic blocks, defined by the indentations
#   - We have a large `while` loop that includes an `if`/`else` block
#   - Then there's another `if`/`else` block outside of the loop
# - It's safe to say that the code within the loop might be executed multiple times, and the one outside will be executed just once

# %%
import random

n_min = 1
n_max = 9
count = 5
win = False

# Setting the secret code once
secret_code = random.randint(n_min, n_max)

print("This is Da Bomb")
print(f"You have {count} tries. The code is between {n_min} and {n_max}")

# This keeps going until count is > 0 and win == False
while count > 0 and not win:

    # Updating the count variable
    count -= 1

    # Getting a guess from the user
    guess = int(input("Guess the secret code: "))
    
    # Checking the guess against the code
    if guess == secret_code:
        win = True
    else:
        print(f"Nope! You have {count} tries left 🙈")

# Communicating the result
if not win:
    print("💥💥💥")
    print(f"The code was {secret_code} btw")
else:
    print("Phew! You've done it! 🕵️‍♂️")

# %% [markdown]
# # Number Guessing Game 🔮
# Write a program where the computer randomly selects a number and the user has to guess it. The program should tell the user if their guess is too high or too low, and continue until the correct number is guessed. (Thanks ChatGPT)

# %%
# Number Guessing Game
import random

secret_number = random.randint(1, 100)
guess = None

print("I'm thinking of a number between 1 and 100. Can you guess it?")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")

# %% [markdown]
# # Time! ⏳
# 
# Let me show you `datetime.now()`.
# It's quite useful to do all things time-related (you don't say?). What it does is it basically returns an *object* (we'll see what it is in a couple notebooks). This object contains lots of time-related values (current year, month, day, hour, minutes, and seconds).

# %%
import datetime
now = datetime.datetime.now()  # now is an "object". The function now() doesn't need inputs
# We use it as below to obtain the variables that describe the time:
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

print("Today is:", year, "/", month, "/", day)
print("The time is:", hour, ":", minute, ":", second)

# %% [markdown]
# And what about `time.sleep()`, which allows us to stop the execution for a given amount of seconds.

# %%
import time

print("Yawn. Think I'll nap 5 seconds!")
time.sleep(5)  # time.sleep() only wants some seconds of us. Oh if everyone was like time.sleep().
print("Hey! Now I feel better!")

# %% [markdown]
# # Exercise 3 - Alarm ⏰
# By combining `datetime.now()` and `time.sleep()` we should be able to build an alarm:
# 
# - Let's ask the user for the hour and minute they want the alarm to go off
# - If the current hour and minute are matching the alarm ones, let's kick it off!
# - You'll probably want to call a new `datetime.datetime.now()` at every loop, otherwise you'll always keep checking the initial time

# %%
# Exercise 3
import datetime
import time

alarm_hour = int(input("Set the alarm hour (0-23): "))
alarm_minute = int(input("Set the alarm minute (0-59): "))

print("Alarm is set!")

while True:
    now = datetime.datetime.now()
    if now.hour == alarm_hour and now.minute == alarm_minute:
        print("Wake up! ⏰")
        break
    time.sleep(10)  # Wait 10 seconds before checking again

# %% [markdown]
# # Pyramid of Asterisks 🎄
# This is quite a common programming exercise. You can play with it and feel like a pharaoh.

# %%
num = int(input("Enter the number of rows: "))
print()  # Print a newline

i = 0
while i < num:
    print("* " * (i + 1))
    i += 1  # This increments the counter

# %% [markdown]
# # Modulo Operator ➗
# 
# The modulo operator `%` returns the remainder of a division.
# For example, `5 % 3` equals `2` because `5 / 3` equals `1` with a remainder of `2`.
# 
# But why am I learning this? What kind of use will it ever have?
# 
# Well, it turns out it's pretty convenient to use modulo with `2`, because it will always return `1` if the number is odd and `0` if it's even.

# %%
# Let's run through some examples
print("4 % 2 =", 4 % 2)
print("6 % 2 =", 6 % 2)
print("8 % 2 =", 8 % 2)
print("5 % 2 =", 5 % 2)
print("7 % 2 =", 7 % 2)
print("9 % 2 =", 9 % 2)

# %% [markdown]
# # Exercise 4 - Pyramid of Asterisks + 🎄🎄
# Like the previous but write normal asterisks on the even rows and another symbol on the odd ones.
# 
# Yep, you'll need the modulo operator for this.

# %%
# Exercise 4
num = int(input("Enter the number of rows: "))
symbol1 = "*"
symbol2 = "#"

i = 0
while i < num:
    if i % 2 == 0:
        print(symbol1 + " " * (i + 1))
    else:
        print(symbol2 + " " * (i + 1))
    i += 1

# %% [markdown]
# # Exercise 5 - Diamond Shape 🎄🎄🎄
# Like the main pyramid but instead of stopping at the base, keep going and write the flipped version. The result will be diamond-shaped.

# %%
# Exercise 5
num = int(input("Enter the number of rows for half of the diamond: "))

# Upper half
i = 1
while i <= num:
    print(" " * (num - i) + "* " * i)
    i += 1

# Lower half
i = num - 1
while i >= 1:
    print(" " * (num - i) + "* " * i)
    i -= 1

# %% [markdown]
# # Exercise 6 - Collatz Conjecture 🤓
# **NERD Alert**
# 
# So [here's](https://www.quantamagazine.org/why-mathematicians-still-cant-solve-the-collatz-conjecture-20200922/) a very nerdy maths article explaining how the Collatz Conjecture works.
# 
# Write a program that implements it and verify that it is indeed true no matter what number you start with.
# 
# *Hint: limit the main loop to a fixed number of iterations, like 100*

# %%
# Exercise 6
num = int(input("Enter a positive integer: "))
iterations = 0
max_iterations = 100

while num != 1 and iterations < max_iterations:
    print(num)
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
    iterations += 1

if num == 1:
    print(num)
    print("Reached 1 after", iterations, "iterations.")
else:
    print("Did not reach 1 after", max_iterations, "iterations.")
