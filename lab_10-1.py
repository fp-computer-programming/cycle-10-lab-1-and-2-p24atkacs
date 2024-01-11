"""

Create a Python file named lab_10-1.py
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Using a while loop, write a program that prompts the user to input a number.
If the user inputs a number, add that to the sum of the previous numbers entered.
If the user enters -1, the program should end and display the sum of all the numbers entered.
Be sure the program uses a break statement
_____________________________________________________________________________________________________________

Create a Python file named lab_10-2.py
Using the same approach as lab 1, write a program that prints all the numbers that are multiples of 3 in a list. Be sure your program uses a continue statement


"""

# Author: Andrew Tkacs

# sum variable to keep track of the sum
total_sum = 0

while True:
    # Prompt user for input
    user_input = int(input("Enter a number (or -1 to end): "))

    # ends the code if the person enters -1
    if user_input == -1:
        break

    # Add the entered number to the sum
    total_sum += user_input

# Display the sum of all entered numbers
print(f"Sum of numbers entered: {total_sum}")
