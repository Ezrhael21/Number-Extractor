# Ezrhael R. Sicat
# BSCpE 1-5
# 04/27/2023
# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; the first text file will be named even.txt 
# that will contains all even numbers extracted from the numbers.txt. The second text file 
# will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

import pyfiglet
font = pyfiglet.figlet_format("Number Extractor", font = "big", justify = "center")
print (font)

# Introduction to the program 
name = input("Enter your username: ")
print ("Hello!", name)
print ("Today, We are going to extract numbers")

# ask user for input
while True:
    user_input = input("How many numbers would you like to input? ")
    # looping to accept only valid number
    if not user_input.isnumeric():
        print("Invalid input. Please enter a valid number.")
    else:
        number_inputs = int(user_input)
        break

numbers = []
i = 0
while len(numbers) < number_inputs:
# ask the user to enter the number
    num = input("Enter number {} of {}: ".format(i+1, user_input))
    # looping to accept only an integer number
    if not (num.isnumeric() or num.startswith('-') and num[1:].isnumeric()):
        print("Invalid input. Please enter a number.")
    else:
        numbers.append(num)
        i += 1

# Time Delay
print ("Extracting...")
import time
time.sleep(5)

# write the numbers to the file
with open("numbers.txt", "w") as number_file:
    number_file.write(",".join(numbers))
    
# read the contents of the file
with open("numbers.txt", "r") as input_file:
    user_numbers = input_file.read().strip().split(",")

# loop through each number and add it to the appropriate list
odd_numbers = []
even_numbers = []
for number in user_numbers:
    if int(number) % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# convert the list into string
odd_numbers_str = ' '.join(odd_numbers)
even_numbers_str = ' '.join(even_numbers)
user_numbers_str = ' '.join(user_numbers)

# display output
print ("User numbers: ", user_numbers_str)
print ("Odd numbers: ", odd_numbers_str)
print ("Even numbers: ", even_numbers_str)

# write odd and even numbers to files
with open("odd.txt", "w") as odd_file, open("even.txt", "w") as even_file:
    odd_file.write("\n".join(odd_numbers))
    even_file.write("\n".join(even_numbers))