# Write a function named welcome_message() that prints “Welcome to 
# Python Programming!” three times. 

def welcome_message():
    for i in range(0,3):
        print("Welcome To Python Programming!")

welcome_message()

# Create a function good_morning() that prints "Good Morning, Saumya!". 
# Call it twice.

def good_morning():
    print("Good Morning, Saumya!")

good_morning()
good_morning()

# Write a function show_age(name, age) that prints: "Saumya Singh is 21 
# years old." 
def show_age(name,age):
    print(f"{name} is {age} years old")
show_age("Saumya",21)

# Create a function add_numbers(a, b) that prints both the sum and 
# difference.
def add(a,b):
    print("Sum is:",a+b)
add(5,10)

# Write a function fav_food(food) that prints "Saumya loves <food>".
def fav_food(food):
    print(f"Saumya loves {food}")
fav_food("Gulab Jamun")

# Define a function convert_to_upper(word) that returns the uppercase 
# version of the string. 
def convert_to_upper(word):
    up_word = word.upper()
    return up_word

word = input("Enter a word: ")
up_word = convert_to_upper(word)
print("Uppercase Word:",up_word)

# Create a function full_name(fname, lname) that returns the full name 
# joined with a space. 
def full_name(fname, lname):
    ful_name = fname + " " + lname
    return ful_name 
fname = input("Enter first name: ")
lname = input("Enter last name: ")
ful_name = full_name(fname,lname)
print("Your Full Name is:",ful_name)

# Define a function message(text="Keep Learning!") and call it with and 
# without an argument. 
def message(text="Keep Learning!"):
    print(text)
message()

# Create a function login(username, password="1234") that prints the 
# credentials. 
def login(username, password="1234"):
    print("Username:",username)
    print("Password:",password)
login("ROhan","56789")

