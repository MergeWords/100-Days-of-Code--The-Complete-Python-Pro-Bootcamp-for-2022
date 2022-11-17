#Data Types:

# Strings
print("Hello"[-1])
print("123" + "345")

# Integer
print(123 + 345)
123_456_789

# Float
3.14159

# Boolean
True
False

# Type Error
num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")
# Type Checking
type(num_char)
# Type Conversion
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = str(123)
print(type(a))

b = float(123)
print(type(b))

# Exercise 1 Data Types
two_digit_number = input("Type a two digit number: ")
print(int(str(two_digit_number)[0]) + int(str(two_digit_number)[1]))

print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)

# Mathematical Operations in Python
3 + 5
7 - 3
3 * 2
6 / 3
print(type(6 / 3))
2 ** 3
# PEMDASLR
# ()
# **
# left to right 
# * /
# left to right 
# + -
print(3 * 3 + 3 / 3 - 3)
print(3 * ((3 + 3) / 3) - 3)

# Exercise 2 - BMI Calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# round(65 / (1.8 ** 2))
# 20
# print(type(weight))
# round(float(weight) / (float(height) ** 2 ))
bmi = round(float(weight) / (float(height) ** 2 ))
print(bmi)

# Number Manipulation and F Strings in Python
print(8 / 3)
print(round(8 / 3))
print(round(8 / 3, 2))
print(round(2.666666, 2))

# floor division
print(8 // 3)
print(type(8 // 3))

# Very handy for when you have to manipulate a value based on it's previous value
result = 4 / 2
print(result)
result /= 2
print(result)

# Keep score in soccer
score = 0
print(score)
# User scores a point
score += 1
print(score)

# f strings
score = 2
height = 1.8
isWinning = True
# manual way
# print("your score is " + str(score) + ", your height is " + str(height) + ", your are winning is " + str(isWinning))
# using f strings
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# Exercise 3 - Life in Weeks
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# https://waitbutwhy.com/2014/05/life-weeks.html
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years = 90
age_minus_years = 90 - int(age)
# print(f"You have {age_minus_years} years")
days_left = age_minus_years * 365
days_left = f"You have {days_left} days"
# print(f"{days_left}, ")
weeks_left = age_minus_years * 52
weeks_left = f"{weeks_left} weeks"
# print(f"{days_left}, {weeks_left}, ")
months_left = age_minus_years * 12
months_left = f"{months_left} months"
result = f"{days_left}, {weeks_left}, and {months_left} left."
print(result)

# Day 2 Project: Tip Calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = float(input("How much tip would you like to give?\n"))
people = float(input("How many people are splitting the bill?\n"))
tip = tip / 100
tip += 1
# print(f"{bill}, {people}, {tip}")
tip_per_person = round((bill / people) * tip, 2)
# print(tip_per_person)
# f-string format to 2 decimal places
# print(f"{tip_per_person:.2f}")
print(f"Each person should pay: ${tip_per_person:.2f}")
