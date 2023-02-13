# User input:

# first_name = "Michael"
# last_name = "Ruiz"
# full_name = first_name + " " + last_name
# print("Hello" + full_name)
# print(type(first_name))
# print(len(last_name))
# print(first_name.find("M"))
# print(first_name.capitalize())
# print(first_name.upper())
# print(first_name.lower())
# print(first_name.isdigit())
# print(first_name.isalpha())
# print(first_name.count("i"))
# print(first_name.replace("c", "p"))
# print(first_name * 4)

## User input:
# name = input("What is your name?: ")
# age = int(input("How old are you?: "))

# age = age + 1

# print("Hello " + name)
# print("You are " + str(age) + " years old")

# import math

# pi = 3.14
# x = 1
# y = 2
# z = 3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(max(x,y,z))
# print(min(x,y,z))

# slicing : create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

# name = "Michael 1024"

# first_name = name[0:6]
# last_name = name[7:11]
# reversed_name = name[::-1]

# print(first_name)
# print(last_name)
# print(reversed_name)

# website = "http://google.com"
# website2 = "http://wikipedia.com"

# slice = slice(7,-4)

# print(website[slice])
# print(website2[slice])

# if statement = a block of code that will execute if it's condition is true.

# age = int(input("How old are you?: "))

# if age >= 18:
#     print("You are an adult!")
# elif age == 100:
#     print("You are a century old!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")

# logical operators (and,or,not) = used to check if two or more conditional statements are true.

# temp = int(input("what is the temperature outside?: "))

# if temp >= 0 and temp <= 30:
#     print("The temperature is good today!")
#     print("go outside!")
# elif temp < 0 or temp > 30:
#     print("The temperature is bad today!")
#     print("stay outside!")

# while loop = a stastement that will execute it's block of code as long as it's condition remains true.

# while 1 == 1:
#     print("Help I am an infinite loop!")

# name = ""

# while len(name) == 0:
#     name = input("Enter your name: ")

# print("Hello " + name)

#import time
# for loop = a statement that will execute it's block of code
#            a limited amount of times
#
#            while loop = unlimited
#            for loop = limited

# for i in range(10):
    #print(i + 1)

# for i in range(50, 100+1, 2):
    #print(i)

# for i in "Bro Code":
    #print(i)

# for seconds in range(10,0,-1):
    # print(seconds)
    # time.sleep(1)
# print("Happy New Year!")

# nested loops = The inner loop will finish all of its' iterations before
#                finishing one iteration of the outer loop
# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# Loop Control Statements = change a loops execution from its normal sequence.

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"

# for i in phone_number:
    #if i == "-":
        # continue
    #print(i, end="")

# for i in range(1, 21):
#     if i == 13:
#         pass
#     else:
#         print(i)

# list = used to store multiple items in a single variable

# food = ["pizza","hamburger","hotdog","spaghetti","pudding"]
# food[0] = "sushi"

#food.append("ice cream")
#food.remove("hotdog")
#food.pop()
#food.insert(0,"cake")
#food.sort()
#food.clear()

# for x in food:
#     print(x)

# 2D lists = a list of lists
# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]

# food = [drinks, dinner, dessert]

# print(food)

# tuple = collection which is ordered and unchangeable
#         used to group together related data

# student = ("Bro", 21, "male")

# print(student.count("Bro"))
# print(student.index("male"))

# for x in student:
#     print(x)

# if "Bro" in student:
#     print("Bro is here")

# set = collection which is unordered, unindexed. No duplicate values

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#dishes.update(utensils)
# dinner_table = utensils.union(dishes)

#print(dishes.difference(utensils))
#print(utensils.intersection(dishes))

# for x in dinner_table:

# dictionary  = A changeable, unordered collection of unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly

# capitals = {'USA': 'Washington DC',
#             'India': 'New Dehli',
#             'China': 'Beijin',
#             'Russia': 'Moscow'}

# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()

# print(capitals)
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key,value in capitals.items():
#     print(key, value)

# function = a block of code which is executed only when it is called.

# def hello(name):
#     print("Hello " + name)
#     print("Have a nice day!")

# hello("Bro")

# return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the function's return value

# def multiply(number1, number2)
#     result = number1 * number2
#     return result

# print(multiply(6,9))

# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created.
# LEGB = Local Enclosing Global Built-in

# name = "Bro" # global scope (available inside & outside functions)

# def display_name():
#     name = "Code"   # local scope and only inside the function
#     print(name)

# display_name()
# print(name)

# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#     return sum

# print(add(1,2,3,4,5,6,7,8))

# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so thawwt a function can accpet a varying amount of keyword arguments

# def hello(**names):
#     # print("Hello " + kwargs['first'] + " " + kwargs['last'])
#     print("Hello", end=" ")
#     for key,value in kwargs.items():
#         print(value,end=" ")

# hello(first="Bro", middle="Dude",last="Code")

# import random

# x = random.randint(1,6)
# y = random.random()

# myList = ['rock', 'paper', 'scissors']
# z = random.choice(myList)

# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

# random.shuffle()

# print(z)






