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

# list of numbers
numbers_list = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27]

#Iterate through the list
for num in numbers_list:
    # Check if the number is not a multiple of 3
    if num % 3 != 0:
        continue

    # Print the number if it is a multiple of 3
    print(num)

