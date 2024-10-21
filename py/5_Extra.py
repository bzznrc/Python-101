# %% [markdown]
# # Functions and Classes 🛠️
# 
# Throughout this course, we've been building a solid foundation in programming using Python. Now, let's explore two fundamental concepts that will empower you to create more complex and organized programs: **Functions** and **Classes**.
# 
# These are the building blocks that allow you to structure your code effectively, making it reusable, modular, and easier to understand.

# %% [markdown]
# ## Functions 🤖
# 
# A **function** is a block of organized, reusable code that performs a single, related action. Functions help break our program into smaller and modular chunks, making it more manageable and reusable.
# 
# Think of functions as little machines: you give them input (parameters), they do some processing, and then they give you output (return value).

# %%
# Example of a simple function without parameters
def greet():
    print("Hello! Welcome to the world of Python.")

# Calling the function
greet()

# %%
# Example of a function with parameters
def greet_person(name):
    print(f"Hello, {name}! How are you today?")

# Calling the function with an argument
greet_person("Alice")

# %%
# Example of a function with a return value
def add_numbers(a, b):
    result = a + b
    return result

# Using the function and printing the result
sum_result = add_numbers(5, 7)
print("The sum is:", sum_result)

# %% [markdown]
# ### Why Use Functions?
# 
# - **Reusability**: Write once, use many times.
# - **Modularity**: Break complex problems into simpler pieces.
# - **Readability**: Makes code easier to read and maintain.
# - **Avoid Repetition**: Reduces redundancy in your code.

# %% [markdown]
# ## Parameters and Arguments 🔡
# 
# - **Parameters** are variables listed in the function's definition.
# - **Arguments** are the actual values passed to the function when you call it.
# 
# For example, in `def greet_person(name):`, `name` is a parameter. When we call `greet_person("Alice")`, `"Alice"` is the argument.

# %% [markdown]
# ## Return Values 📦
# 
# A function can send back a value using the `return` statement. This allows you to capture the output and use it elsewhere in your code.

# %%
# Function that checks if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Using the function
number_to_check = 4
if is_even(number_to_check):
    print(f"{number_to_check} is even.")
else:
    print(f"{number_to_check} is odd.")

# %% [markdown]
# ## Scope 🧐
# 
# **Scope** refers to the visibility of variables. Variables created inside a function are **local** to that function and cannot be accessed outside of it. Variables created outside of functions are **global** and can be accessed anywhere in the code.

# %%
# Global variable
x = 10

def multiply_by_two():
    # Local variable
    y = x * 2
    print("Y inside function:", y)

multiply_by_two()
# print(y)  # This would cause an error because y is not defined outside the function

# %% [markdown]
# ## Classes and Objects 🧱
# 
# Python is an **object-oriented programming (OOP)** language. This means it allows us to create objects that model real-world things.
# 
# - A **class** is like a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class can have.
# - An **object** is an instance of a class. It's a specific realization of the class with actual values.
# 
# ### Why Use Classes?
# 
# - **Organization**: Helps to organize code into logical and manageable structures.
# - **Reusability**: Once a class is defined, multiple objects can be created from it.
# - **Abstraction**: Can model complex systems more naturally.

# %%
# Defining a class
class Person:
    # The __init__ method initializes the object's attributes
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute
    
    # Method to greet
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Creating objects (instances of the class)
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Using methods
person1.greet()
person2.greet()

# %% [markdown]
# ### Adding Methods to Classes
# 
# Methods are functions that belong to an object. They can perform actions using the object's attributes.

# %%
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hi, I'm {self.name}.")
        
    def is_adult(self):
        if self.age >= 18:
            print(f"{self.name} is an adult.")
            return True
        else:
            print(f"{self.name} is not an adult.")
            return False

# Create an instance
person = Person("Charlie", 17)
person.greet()

# Check if the person is an adult
person.is_adult()

# %% [markdown]
# ## Exercises 📝
# 
# ### Exercise 1: Age Checker 👶👴
# 
# - Write a function `check_age` that takes a name and age as parameters.
# - The function should print a message stating whether the person is a minor or an adult.

# %%
def check_age(name, age):
    if age >= 18:
        print(f"{name} is an adult.")
    else:
        print(f"{name} is a minor.")

# Test the function
check_age("Diana", 20)
check_age("Ethan", 15)

# %% [markdown]
# ### Exercise 2: Person Class Extension 🧑‍💼
# 
# - Add a method `years_to_retirement` to the `Person` class.
# - Assume retirement age is 65.
# - The method should calculate and print how many years the person has until retirement.

# %%
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hi, I'm {self.name}.")
        
    def is_adult(self):
        return self.age >= 18
    
    def years_to_retirement(self):
        retirement_age = 65
        years_left = retirement_age - self.age
        if years_left > 0:
            print(f"{self.name} has {years_left} years until retirement.")
        else:
            print(f"{self.name} is already retired.")

# Create instances and test the new method
person1 = Person("Emma", 30)
person2 = Person("Frank", 70)

person1.years_to_retirement()
person2.years_to_retirement()

# %% [markdown]
# ### Exercise 3: Contact List 📇
# 
# - Create an empty list called `contacts`.
# - Ask the user if they want to add a new contact.
# - If they do, ask for the contact's name and phone number, and create a `Person` object with an additional attribute `phone_number`.
# - Add the new contact to the `contacts` list.
# - Repeat until the user doesn't want to add more contacts.
# - At the end, print out all contacts with their details.

# %%
class Person:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        
    def display_contact(self):
        print(f"Name: {self.name}, Age: {self.age}, Phone: {self.phone_number}")

# Create an empty list for contacts
contacts = []

# Loop to add contacts
while True:
    add_contact = input("Do you want to add a new contact? (yes/no): ").lower()
    if add_contact == 'yes':
        name = input("Enter contact's name: ")
        age = int(input("Enter contact's age: "))
        phone_number = input("Enter contact's phone number: ")
        contact = Person(name, age, phone_number)
        contacts.append(contact)
    else:
        break

# Display all contacts
print("\nContact List:")
for contact in contacts:
    contact.display_contact()

# %% [markdown]
# ## The Bigger Picture 🌍
# 
# Congratulations on making it this far! You've learned about:
# 
# - **Variables** and **Data Types**
# - **Operators**
# - **Control Flow** with `if`, `elif`, `else`
# - **Loops**: `for` and `while`
# - **Lists** and **Dictionaries**
# - **Functions**
# - **Classes and Objects**
# 
# These concepts are the fundamental building blocks of programming. With them, you can create a vast array of programs, from simple scripts to complex applications.

# %% [markdown]
# ## Where to Go from Here? 🚀
# 
# The world of programming is vast and exciting. Here's how you can apply what you've learned and explore different areas:
# 
# ### 1. Game Development 🎮
# 
# - **Pygame**: A popular library for making games in Python.
# - Start with simple games like Snake or Tetris.
# - Learn about graphics, animations, and user input.
# 
# ### 2. Web Development 🌐
# 
# - **Backend Development**: Use frameworks like Flask or Django to build web applications.
# - **Frontend Development**: Learn HTML, CSS, and JavaScript to create interactive user interfaces.
# 
# ### 3. Data Science and Machine Learning 📊🤖
# 
# - **Data Analysis**: Use libraries like Pandas and NumPy to manipulate and analyze data.
# - **Visualization**: Matplotlib and Seaborn for creating graphs and charts.
# - **Machine Learning**: Scikit-learn for algorithms, TensorFlow or PyTorch for deep learning.
# 
# ### 4. Desktop Applications 🖥️
# 
# - **GUI Development**: Create desktop applications using Tkinter or PyQt.
# - Build tools with graphical interfaces.
# 
# ### 5. Automation and Scripting 🤖
# 
# - Automate repetitive tasks.
# - Write scripts for file management, web scraping, and more.
# 
# ### 6. Mobile Development 📱
# 
# - **Kivy**: A framework for building cross-platform mobile apps in Python.
# 
# ## Tips for Learning More 📚
# 
# - **Build Projects**: The best way to learn is by doing. Start small and gradually increase complexity.
# - **Join Communities**: Participate in forums like Stack Overflow or Reddit's r/learnpython.
# - **Online Courses**: Platforms like Coursera, edX, and Udemy offer courses on various topics.
# - **Read Documentation**: Familiarize yourself with official documentation and tutorials.
# - **Stay Curious**: Technology evolves rapidly. Keep learning and exploring new concepts.
# 
# ## Final Thoughts 🎉
# 
# Programming is a journey of creativity and problem-solving. The skills you've acquired are just the beginning. Whether you're interested in developing the next hit game, analyzing complex data, or automating tasks, Python provides the tools you need.
# 
# Remember, every expert was once a beginner. Keep experimenting, stay persistent, and most importantly, have fun!
# 
# Happy coding! 👩‍💻👨‍💻
