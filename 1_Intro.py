# %% [markdown]
# # Algorithm ⚗
# An algorithm is a step-by-step procedure or a set of rules to solve a specific problem or accomplish a certain task. It's like a recipe in cooking or directions on a GPS.
# 
# Let's take the example of a recipe. If you want to bake a cake, the recipe will provide you with a list of ingredients you need and instructions on what to do with those ingredients, in a specific order. That's essentially what an algorithm is—a recipe for your computer to follow in order to achieve a desired outcome.
# 
# In the context of programming, an algorithm could be a process for sorting a list of numbers from smallest to largest, finding the shortest path between two points on a map, or searching for a specific item in a database.
# 
# Just like in a recipe, the order of the steps in an algorithm is very important. A small change in the order can lead to a completely different result.
# 
# Also, a good algorithm is one that solves a problem efficiently and effectively, meaning it does the job correctly and as quickly as possible, using the least amount of computing resources.
# 
# <img src="https://media.gcflearnfree.org/content/5be1de13686707122ccd266f_11_06_2018/algorithms_illustration.jpg" width="500" height="300">

# %% [markdown]
# # Program 🤖
# > A program is the implementation of an algorithm in a programming language.
# 
# Programming a computer to solve a problem always requires defining data to represent the things in your problem; this is called modeling. It also requires explaining unambiguously what process to follow in order to solve the problem.
# 
# In imperative programming (ours and the most well-known), we tell the computer what to do to the data. The computer starts out with its memory containing stuff; we tell it how to change that stuff, and it makes those changes.
# 
# A program is run, one line at a time, from top to bottom. This seems silly but it's actually very important to keep in mind at all times.
# 
# Usually, you can identify:
# 
# - **Inputs**: Data that goes in
# - **Logic**: What happens to the data
# - **Outputs**: Results that come out

# %%
# 1 - INPUT - Asking for data
lire = input("Insert a LIRE amount: ")

# 2 - LOGIC (is usually quite longer)
eur = float(lire) / 1936.27

# 3 - OUTPUT - Communicating the result
print("EUR:", eur)

# %% [markdown]
# # Python 🐍
# 
# *Python is an interpreted, high-level, and general-purpose programming language.*
# 
# *Python's design philosophy emphasizes code readability with its notable use of significant whitespace.*
# 
# There are two main approaches to Python programming:
# 
# **File .py** - Code written on an **IDE** (*Integrated Development Environment*, which is an application such as Visual Studio Code, that needs to be installed beforehand) and executed by a **Python interpreter** (that needs to be installed as well). Everything happens on your local machine. This is the classical way of executing code.
# 
# **Online notebooks** - .ipynb files (such as this one) that contain both code and text. The code gets executed on a pre-configured cloud server, which means the user is not required to install anything locally. This started being used in the scientific community to communicate effectively what happens with the code step by step, and it's now widely used with most of the computation moving to the cloud.

# %% [markdown]
# # We are Coders (but also Users) 🤠
# Traditionally, who writes the code (the programmer) and who executes it (the user) are distinct roles, and the user doesn't get to access the source code.
# 
# Working on a notebook is a bit different as these roles get mixed up, with the user being able to change the code as well. Building our first programs, we'll need to keep in mind that we're programmers when we write and users when we execute. This way, it makes sense that we (as programmers) ask ourselves (as users) to input some data to the program.
# 
# Just try not to develop any additional personality.

# %% [markdown]
# # IDEs & Reading Code 📑
# 
# A Python (.py) file is essentially text. You can actually change its extension to .txt and it will open to display the code as text.
# 
# We don't code with text files and notepads; we use IDEs (Integrated Development Environments, like Visual Studio Code). An IDE is basically a notepad on steroids; it allows us to write code and gives us all sorts of tools to check it and test it.
# 
# An important thing (which might seem silly, but trust me IT'S-SO-IMPORTANT) is that it color-codes every word for us, based on its meaning. Let's see some examples (and, just to be clear, the code below doesn't make any sense):

# %%
# GREEN - Comment. This is a special line that gets ignored by the interpreter. You can write what you want here!
a = 2  # WHITE - Variables and numeric values. We'll see what they are in a bit
b = 'Hey'  # ORANGE - Text values, called "strings". They have to be surrounded by quotes (or double quotes)
c = True  # BLUE - Boolean values. They can be True/False. We'll use them to write our logic
print('I am a bit confused')  # YELLOW - Functions. They call other chunks of code to do some stuff for us. We'll see a few
for i in range(5): pass  # PURPLE - Statements (if, while, for...). They are used to control how code flows
d = int(input("How confused from 1 to 10? ")) / 2  # BLUE/GREEN - Casts, ways to change the type of a variable

# %% [markdown]
# # Print 📃
# Let's have a look at some syntax (*yayyy syntax!* said no one ever).
# 
# `print` shows a text string (which is the text between quotes) in the output.
# The "output" for us is the area below the code, but it's a generic term for whatever communication channel you have with the user. It can mean a webpage if we are writing a web app, or a pop-up window if we're building a GUI (Graphical User Interface).
# 
# `print` writes back all that we give it as an *argument* (which is everything that's enclosed within the print brackets). We can pass text or variables to it, and every argument has to be separated by commas.
# 
# Let's see some examples:

# %%
print('I can type what I want here and then execute this. Just click the play button on the left!')

# %%
# Have fun writing random print statements here!
print('Hello, world!')
print('Python is fun!')
print('Let\'s learn together!')

# %% [markdown]
# ### "Quotes"
# Funny thing about quotes. You have double quotes (" ") and single ones (' '). You can use either, just use the same for the start and end of a string (so no mixing " ' or ' ").
# 
# Sometimes you'll want to type something that contains a quote mark, like the previous statement. If you used single quotes for it, Python would get quite confused, but you can always use the other ones:

# %%
# Error incoming. Actually, you can see that the first quote splits the string into an orange portion and a white one, which Python doesn't really know what to do with
# print('Sometimes you'll want to type something that contains a quote mark')

# %%
# This is how you write it; just swap the first and last quotes with double ones
print("Sometimes you'll want to type something that contains a quote mark")

# %% [markdown]
# # Variables and Operations 📦
# Variables are essentially containers for stuff. We'll define a name for each of them, and we can assign both a numerical or text value to a variable.
# 
# We can reassign a value to a variable that contains a value already, even if the type of the new variable is different from the old one. In that case, the previous value gets forgotten, and the variable is equal to the new one from then on. That's something pretty transparent in Python, but most other programming languages prevent you from doing so.
# 
# We could also assign the result of a mathematical operation to a variable, even if the operation is between other variables (yep, we can get into an Inception situation pretty fast here).

# %%
# Creating an 'a' variable and printing "a equals" followed by the value of the 'a' variable
a = 2
print('a equals:', a)

# Creating a 'b' variable and printing "b equals" followed by the value of the 'b' variable
b = 5
print('b equals:', b)

# Creating a 'c' assigning to it the result of a + b, then printing it
c = a + b
print('c equals:', c)

# The 'a' variable existed already. We're now replacing its value with the double of what it was
a = a * 2
print('a (times):', a)

# The same 'a' variable now will contain a text string. Python doesn't really care much
a = 'sushi'
print('a (string):', a)

# You could even multiply text by some number. Not something you'll probably do often
a = a * 2
print('a (string times):', a)
b = 'tempura'
print('b (string):', b)

# I mean, I would really question this if I saw it in some code, but still you could do it
c = a + b * 4
print('c (string times):', c)

# %% [markdown]
# # Inputs ✏
# `input` stops the program execution and waits for the user to insert a value from the *input* (which, like the output, might mean different things, but in our case it's just a box that pops up below the code). We can then assign this value to a variable.
# 
# `input` is pretty much the opposite of `print`.

# %%
my_text = "noodles"
print("I don't like", my_text)

# %%
# 'my_text' variable contains a value already. When the input runs, the value gets overwritten and then the print displays it
my_text = input("What is that you like then? ")
print("Oh I like", my_text)

# %% [markdown]
# # Cast ⚒
# Programming seems fun, right?
# 
# It isn't. Programming is dealing with things not behaving like you expect 95% of the time.
# 
# Well, that might sound a bit dramatic. Actually, programming is fun. But also frustrating. But also fun. But also frustrating.
# 
# An example of this is what happens when you run the first bit of code below.
# 
# Seems pretty straightforward, right? We ask for a Lire amount from the user, convert it to Euros with the conversion constant, and display it back. What could possibly go wrong?
# 
# What about the program thinking that the Lire amount the user inserts is a text string instead of a number, and thus crashing because it thinks we asked it to divide a text string by a decimal number?
# 
# Yup. By default, `input()` returns a **text string**. If I input 40000, what ends up in the variable `lire` is `"40000"`, which is a text string containing the text `"40000"`. Not the number 40000 (big difference).
# 
# What we should do here is apply a **cast** function, which is a function that changes the type of a variable (turning the text `"40000"` into the number `40000`, for example).
# 
# There are many cast functions, and they are made up from the type the variable needs to be cast to, then the current variable within the brackets.
# 
# In our case, we'll use `float()` to turn the value into a decimal number. If we need to, we could also use `int()` to transform into an integer number or `str()` to turn something into a text string.

# %%
# Brace for impact
lire = input("Insert a LIRE amount: ")
# The following line will cause an error because 'lire' is a string
# eur = lire / 1936.27
# print("EUR:", eur)

# %%
# Phew
lire = float(input("Insert a LIRE amount: "))
eur = lire / 1936.27
print("EUR:", eur)

# %% [markdown]
# # Exercise 1 - 😸
# Create a variable (you can call it however you like) and assign to it the string `"I like pasta"`, then print it.

# %%
pasta_love = "I like pasta"
print(pasta_love)

# %% [markdown]
# # Exercise 2 - 😼
# Write the string from the previous exercise 100 times. In a smart way.
# 
# Please don't type it a hundred times; I would feel so guilty lol.

# %%
print((pasta_love + ' ') * 100)

# %% [markdown]
# # Exercise 3 - 🙀
# - Ask the user for their favourite pasta type and store the string in a variable
# - Ask the user for a 1 to 10 score of how much they like it and store it into another variable
# - Print out their favourite pasta times the score they chose

# %%
# Ask the user for their favourite pasta type
fav_pasta = input("What is your favourite pasta type? ")

# Ask the user for a 1 to 10 score
score = int(input("On a scale of 1 to 10, how much do you like it? "))

# Print out their favourite pasta times the score
print((fav_pasta + ' ') * score)

# %% [markdown]
# # Exercise 4 - 📐
# - Ask the user for the base and height of a triangle and store them
# - Print out the area of the triangle
# 
# *Hints: You need more than 1 variable. Also a couple of casts.*

# %%
# Ask the user for base and height of a triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area of the triangle
area = 0.5 * base * height

# Print out the area of the triangle
print("The area of the triangle is:", area)

# %% [markdown]
# # WAAAIT, what about ChatGPT? 🧞‍♀️
# Why am I learning all this? Can't we just have it write code for us?
# 
# Well, I asked ChatGPT (obviously):
# 
# > While AI like ChatGPT can generate code snippets and assist with coding tasks, there are several reasons why learning to code yourself is still important:
# 
# > **Understanding**: AI can generate code, but it's crucial for you to understand what the code is doing. This understanding allows you to debug, optimize, and modify the code as per your requirements.
# 
# > **Customization**: Every project is unique, and while AI can provide general solutions, it may not always be able to cater to specific project needs. Knowing how to code allows you to customize solutions for your exact requirements.
# 
# > **Problem Solving**: Coding is not just about writing code; it's about problem-solving and logical thinking. These skills are universally applicable and valuable in many areas beyond coding.
# 
# > **Control**: AI models like GPT-3 are tools that can assist you, but they don't replace the need for a human to control and direct what's happening. You need to be able to guide the process and make decisions.
# 
# > **Learning and Growth**: The field of technology is always evolving. By learning to code, you keep up with these changes and open up opportunities for personal and professional growth.
# 
# > **Reliability**: AI can sometimes produce incorrect or inefficient code. Knowing how to code allows you to verify the accuracy and efficiency of the code.
# 
# > Remember, AI is a tool designed to assist and enhance human capabilities, not replace them.
