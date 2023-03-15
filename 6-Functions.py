#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UO269412
#
# Created:     20/11/2018
# Copyright:   (c) UO269412 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Exercise 1: Write the following funtions:
# read integer prompts the user to enter an integer number and returns it.
# biggest given two numbers, returns the biggest one.

def read_integer():
    the_integer = int(raw_input("Give me an integer number: "))
    return the_integer
the_number=read_integer()
print("User's number is {}".format(the_number))

def biggest():
    first_number = int(raw_input("Give me the first number: "))
    second_number = int(raw_input("Give me the second number: "))
    if first_number>second_number:
        return first_number
    else:
        return second_number
biggest_number=biggest()
print("The biggest number is {}".format(biggest_number))

# Exercise 2: Using docstrings, document the functions in the previous exercise
"""Help on function read integer in module main :
read integer()
This function prompts the user to enter an integer number using standard input and then, returns
it"""

def read_integer():
    the_integer = int(raw_input("Give me an integer number: "))
    return the_integer
the_number=read_integer()
print("User's number is {}".format(the_number))

def biggest():
    first_number = int(raw_input("Give me the first number: "))
    second_number = int(raw_input("Give me the second number: "))
    if first_number>second_number:
        return first_number
    else:
        return second_number
biggest_number=biggest()
print("The biggest number is {}".format(biggest_number))

# Exercise 3: Using the previous functions write a main program to find the
# biggest of three numbers

def biggest():
    first_number = int(raw_input("Give me the first number: "))
    second_number = int(raw_input("Give me the second number: "))
    if first_number>second_number:
        return first_number
    else:
        return second_number
number_def=biggest()
third_number = int(raw_input("Give me the third number: "))
if number_def>third_number:
    biggest_number = number_def
else:
    biggest_number = third_number
print("The biggest number is {}".format(biggest_number))

# Exercise 4: Write a function that, given a year, returns true if it is a
# leap year; false otherwise. Then, write a main program to check for every year
# from 0 B.C. to now if it is a leap year or not and print a message
# in the way

def leap_year(year):
    if year%4==0 or (year%100==0 and year%400==0):
        return True
    else:
        return False
import time
for i in range(0,2019):
    year = leap_year(i)
    if year:
        print (str(i) + " is a leap year")
    else:
        print (str(i) + " is not a leap year")
t1=time.time()
print(t)

import time
for i in range(0,2019):
    if i%4==0 or (i%100==0 and i%400==0):
        leap_year = True
    else:
        leap_year = False
    if leap_year:
        print (str(i) + " is a leap year")
    else:
        print (str(i) + " is not a leap year")
t2=time.time()
print(t1-t2)

# Exercise 5: : Write a function that, given a student’s mark (number), returns
# ”F” [0,5), “E” [5,6),”D” [6,7),”C” [7,8), ”B” [8,9), ”A” [9,10) or ”A+” (=10)
# Write a main program that asks the user to type a number in the range [0-10]
# and then prints the mark.

def students_mark(mark):
    if mark>= 0 and mark<5:
        return "F"
    elif mark >=5 and mark<6:
        return "E"
    elif mark>=6 and mark<7:
        return "D"
    elif mark>=7 and mark<8:
        return "C"
    elif mark>=8 and mark<9:
        return "B"
    elif mark>=9 and mark<10:
        return "A"
    else:
        return "A+"
number = int(raw_input("Enter your mark: "))
while number<0 or number>10:
    print("The mark must be between 0 and 10")
    number = int(raw_input("Enter your mark: "))
result = students_mark(number)
print("Your mark is {}".format(result))

# Exercise 6: Write a function that returns the nutritional status
# (or body mass index BMI) of a person according to the following table.
# The function will take two parameters weight (in kilos) and height
# (in metres).

def nutritional_status():
    height=float(raw_input("Enter your height in metres: "))
    weight=float(raw_input("Enter your weight in kilos: "))
    BMI=weight/(height**2)
    return BMI
BMI = nutritional_status()
if BMI<18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<25.00:
    print("Normal")
elif BMI>=25.00:
    if BMI>=30.00:
        print("Obese")
    else:
        print("Overweight")

# Exercise 7: Write a function to get the distance from a point, given its x
# and y coordinates, to the origin. Then, write a main program to ask the user
# to enter the cartesian coordinates of a point in a plane and print the
# distance from that point to the axis origin. If you need help to use the math
# module, go to Python online documentation website:
# https://docs.python.org/2/library/math.html

import math
def distance(x, y):
    c = x**2+y**2
    d = c**0.5
    return d
x = int(raw_input("Enter the x coordinate: "))
y = int(raw_input("Enter the x coordinate: "))
result = distance(x,y)
print("The distance is " + str(result))

# Exercise 8: Using the previous function, write another function that returns
# the length of a circle whose center is the origin and passes through a point
# in the plane. To determine the length, you can use the value of π
# imported from the math module (pi). Write a program that prompts for the
# Cartesian coordinates of the point and displays the length of the circle
# centered in the origin and passing through that point.

import math
def distance(x, y):
    auxiliar = x**2+y**2
    radio = auxiliar**0.5
    return radio
x = int(raw_input("Enter the x coordinate: "))
y = int(raw_input("Enter the x coordinate: "))
result = distance(x,y)
final_result = 2*result*math.pi
print("The distance is " + str(final_result))

# Exercise 9: Write a function that, given a positive integer number, returns
# its semi-factorial. Write a main program to test it.

def semifactorial(x):
    sum = 1
    for i in range(2,x+1,2):
        sum = sum * i
    return sum

number=int(raw_input("Enter the number you want to operate: "))
result=semifactorial(number)
print("The semifactorial of the number you've entered is "+ str(result))

# Exercise 10: Write a function that, given a positive integer number,
# calculates the sum of all its proper divisors. Then write a main program
# that asks the user to enter a positive integer and determines if the number
# is a perfect number. Then it prints a message in this way.

def divisors(x):
    sum = 0
    for i in range(1,x+1):
        if x%i==0:
            sum = sum + i
    return sum
number = int(raw_input("Enter your number: "))
while number<0:
    number = int(raw_input("Enter your number: "))
result = divisors(number)
print("The sum of all divisors is "+ str(result))

# Exercise 11:  Write a program to print all the perfect numbers in the range
# [1,limit], where limit is a positive integer typed by the user.

def perfect_number(x):
    list=[]
    for i in range (2,x):
        if x%i!=0:
            list.insert[i]
    return list
x = int(raw_input("Enter the limit: "))
result = perfect_number(x)
print(result)

# Exercise 12: Write a function, isprime(. . .), that returns true if a given
# integer is prime and false otherwise. Then, write a program that asks the user
# to enter a positive integer and displays whether it is not prime. The
# program will keep asking numbers until the number is 0 or negative.

def isprime(x):
    for i in range(2,x):
        if x%i==0:
            return False
        else:
            return True
x = int(raw_input("Enter the number: "))
result = isprime(x)
if result == True:
    print (str(x) + " is a prime number")
else:
    print(str(x) + " is not a prime number")

# Exercise 13: Write a function, to find the n^th term in the following serie:
# Then, write a main program that asks the user to enter values for b
# (first term in the series), c and d, as well as the term to calculate
# (positive integer). Finally, the program must print the value.

# Exercise 14: Write a function, that, given two positive integers, the second
# in the range [2, 16], calculates the first number in the base represented by
# the second and then returns this number as a string. Write a program
# that asks the user to enter a positive integer and prints it in
# base: 2, 8, 10 and 16.

# Exercise 15: Consider the function line(ch, n) below that returns a string
# with n characters ch.
# 1. Write a function square(ch, n) that prints a square with n lines and n
# columns full of characters ch. To get the best possible square, print double
# characters per line.
# 2. Write a main program that asks character and number and then print the
# squared in the way described before.

def line(ch, n):
    for i in range(n+1):
        string = string + ch
        return string
def square (ch, n):
    string = ""
    for i in range(n):
        for j in range(n):
            string = string + ch
        string = string + "\n"
    return string

number = int(raw_input("Enter the number of rows of the square: "))
character = raw_input("Enter the character of the square: ")
result = square(character, n)
print result

# Exercise 16: Write a main program, similar to the previous one, to print
# just the outline of the square. For example, print outlineSquare(”*”, 3):

def outlineSquare(ch, n):
    string = ""
    for i in range(n):
        if i==0 or i==(n-1):
            for j in range(n):
                string = string + ch
            string = string + "\n"
        else:
            for j in range(n):
                if j-1 == 0:
                    string = string + ch
                if (n-1)-j==0:
                    string = string + ch
                else:
                    if j!=0:
                        string = string + " "
            string = string + "\n"
    return string

number=int(raw_input("Enter the number: "))
character=raw_input("Enter the character: ")
result = outlineSquare(character, number)
print result

# Exercise 17: Write a function called fibonacci(n) that return the
# nth term in the Fibonacci series. Then write a main program to test it.

def fibonacci(n):
    sum = 1
    for i in range(1,n-1):
        sum = sum + i
    if n==1:
        sum = 1
    elif n==2:
        sum = 1
    return sum

number = int(raw_input("Enter the position you want to know: "))
result = fibonacci(number)
print result








