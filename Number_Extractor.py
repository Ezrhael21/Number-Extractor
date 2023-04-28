# Ezrhael R. Sicat
# BSCpE 1-5
# 04/27/2023
# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; the first text file will be named even.txt 
# that will contains all even numbers extracted from the numbers.txt. The second text file 
# will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

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

# write the numbers to the file
with open("numbers.txt", "w") as number_file:
    number_file.write(",".join(numbers))
    
# read the contents of the file
# loop through each number and add it to the appropriate list
# convert the list into string
# display output
# write odd and even numbers to files