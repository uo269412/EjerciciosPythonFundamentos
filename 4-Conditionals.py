#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      javie
#
# Created:     08/11/2018
# Copyright:   (c) javie 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Exercise 1:

x=0
if x>=0:
    x=x+1
elif x>=1:
    x=x+2
print ("x=%d"%x)

x=0
if x>=0:
    x=x+1
if x>=1:
    x=x+2
print ("x=%d" %x)

# Exercise 2: Write a program that prompts the user to enter three integer
# numbers and writes a message if they are in ascending order.

first_number = int(raw_input("Enter the first number: "))
second_number = raw_input("Enter the second number: ")
third_number = raw_input("Enter the third number: ")

if c > b > a:
    print ("They are in ascending order")

# Exercise 3: Write a program that prompts the user to enter five integer
# numbers and choose the greatest one.

first_number = raw_input("Enter the first number: ")
second_number = raw_input("Enter the second number: ")
third_number = raw_input("Enter the third number: ")
forth_number = raw_input("Enter the forth number: ")
fifth_number = raw_input("Enter the fifth number: ")

if first_number> second_number and first_number > third_number and first_number > forth_number and first_number > fifth_number:
    print (first_number)
elif second_number> first_number and second_number > third_number and second_number > forth_number and second_number > fifth_number:
    print (second_number)
elif third_number> first_number and third_number > second_number and third_number > forth_number and third_number > fifth_number:
    print (third_number)
elif forth_number> first_number and forth_number > third_number and forth_number > second_number and forth_number > fifth_number:
    print (forth_number)
elif fifth_number> first_number and fifth_number > third_number and fifth_number > second_number and fifth_number > forth_number:
    print (fifth_number)

# Exercise 4: Write a program to solve any first degree equation in the way:
# ax+b=0, where x is the unknown and a and b two real numbers entered by the user.

a = raw_input("Enter the a: ")
b = raw_input("Enter the b: ")
x = -b/a
print(x)

# Exercise 5: Write a program that reads an integer number and prints a menu
# with the following three options: “Calculate the square of the number”,
# “Calculate the cube of the number” and “Calculate 2 times the number”.
# Each option has a letter. The user enters a letter and, depending on this letter,
# the program will do the appropriate operation, showing the result to the user.

input = raw_input("Enter your choice")
print("Type a for square, b for cube and c for 2 times")
if input == a:
    print (input**2)
elif input == b:
    print (input**3)
elif input == c:
    print (input*2)

# Exercise 6: Write a program that prompts the user to enter 4 integer numbers
# in the range [0-100] (representing the marks of a student in different tests)
# and calculate the average mark. Finally, the program will write the average
# mark and the letter associated with this mark, according with the
#following table:

first_mark = raw_input("Enter the first mark: ")
second_mark = raw_input("Enter the second mark: ")
third_mark = raw_input("Enter the third mark: ")
forth_mark = raw_input("Enter the forth mark: ")
average = (first_mark + second_mark + third_mark + forth_mark)/4
if average < 60:
    print ("E")
elif 60 <= average < 70:
    print("D")
elif 70 <= average < 80:
    print("C")
elif 80 <= average < 90:
    print("B")
elif 90 <= average <= 100:
    print ("A")

#Exercise 7: Write a program that prompts a user to enter a year (integer
# number) and determines if this year is or not a leap year.

year = int(raw_input("Enter the year: "))

if (year%4 == 0 and year %100 != 0) or (year %4 == 0 and year %4 == 100 and year % 400):
    print ("It is a leap year")
else:
    print ("It is not a leap year")

# Exercise 8: Modify the previous program such that it also reads the number of
# a month (1 to 12) and shown the number of days in that month depending on the
# month and year introduced.
year = int(raw_input("Enter the year: "))
month = str(raw_input("Enter the month: "))

if month != "february":
    if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "octobre" or month == "decembre":
        print ("The month has 31 days")
    else:
        print ("The month has 30 days")
if (year%4 == 0 and year %100 != 0) or (year %4 == 0 and year %4 == 100 and year % 400):
    print ("It is a leap year")
    print ("The month has 28 days")
else:
    print ("It is not a leap year")
    print ("The month has 27 days")

# Exercise 9: Write a program that prompts the user to enter the coefficients
# of a second degree equation and prints the roots (if they exist)

a = raw_input("Enter the a: ")
b = raw_input("Enter the b: ")
c = raw_input("Enter the c: ")

first_root = str(-b+sqrt(b**2-4*a*c)/(2*a))
second_root = str(-b-sqrt(b**2-4*a*c)/(2*a))

print ("The equation has the roots: " + first_root + " and " + second_root)