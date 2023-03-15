#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UO269412
#
# Created:     23/10/2018
# Copyright:   (c) UO269412 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# Exercise 1: Which is the final value of variable x?

x=0
n=16
while n % 2 == 0:
    x = x + 1
    n = n / 2

# The final value for x is 4

# Exercise 2: Write a program that computes and displays the sum of all
# integers from 1 to an ending number. Prompt the user for the ending number
# that must be greater than 0.

ending_number = int(raw_input("Enter the ending number(greater than zero: "))
while ending_number < 0:
    print("Invalid number, try again")
    ending_number = int(raw_input("Enter the ending number(greater than zero: "))
total_sum = 0
actual_number = 1
while actual_number < ending_number:
    total_sum = total_sum + actual_number
    actual_number = actual_number + 1
print("The sum is: {}".format(total_sum))

# Exercise 3: Write a program that computes and displays the multiplication of
# all integers from 1 to an ending number. Prompt the user for the ending
# number that must be greater than 0.

ending_number = int(raw_input("Enter the ending number(greater than zero: "))
total_multiplication = 1
actual_number = 1
while ending_number > actual_number:
    actual_number = actual_number + 1
    total_multiplication = total_multiplication * actual_number
print("The multiplication is: {}".format(total_multiplication))

# Exercise 4: Write a program that reads a number n > 0, and writes n asterisks.
# Sample output for n = 3:

n = int(raw_input("Enter a number greater than 0: "))
while n <= 0:
    print("Invalid number, try again")
    n = int(raw_input("Enter a number greater than 0: "))
if n > 0:
    print(n * ("*"))

# Exercise 5: Write a program that prints all numbers between 20 and 10
# in descending order.

n = 20
while n >= 10:
    print(n)
    n = n - 1

# Exercise 6: Write a program that prints all even numbers between 40 and 20
# in descending order.

n = 40
while n >= 20:
    while n%2 == 0:
        print(n)
        n = n - 1
    n = n - 1

# Exercise 7: Write a program that prints all multiples of 3 less than 100.

n = 1
while n <= 100:
    while n % 3 == 0:
        print(n)
        n = n + 1
    n = n + 1

# Exercise 8: Write a program that computes the following mathematical
# expression:

i = 1
n = ((i**2+1)/(i))
solution = 0
while i <= 100:
    solution = solution + n
    i = i + 1
print("The solution is {}".format(solution))

# Exercise 9: Change the previous program to prompt the user for the limits of the
# summation variable i (lower_limit and upper_limit) and calculates and prints
# the mathematical expression again. Take into account:
# ? lower_limit and upper_limit must be integers greater than 0
# ? upper_limit must be greater than or equal to lower_limit

solution = 0
lower_limit = int(raw_input("Enter the lower limit: "))
while lower_limit<=0:
    print ("You have entered a below equal or below than zero. Enter the number again")
    lower_limit = int(raw_input("Enter the lower limit: "))
upper_limit = int(raw_input("Enter the upper limit: "))
while upper_limit<=0:
    print ("You have entered a below equal or below than zero. Enter the number again")
    upper_limit = int(raw_input("Enter the upper limit: "))
for i in range (lower_limit, upper_limit+1):
    solution = solution + ((lower_limit**2+1)/(lower_limit))
print("The solution is {}".format(solution))

# Exercise 10: Write a program that reads input from keyboard one character
# at a time until the user enters ".". Then, the program must display
# the number of "a" at the input.

count_of_a = 0
character = raw_input("Enter the character: ")
while character != ".":
    if character == "a":
        count_of_a = count_of_a + 1
    character = raw_input("Enter the character: ")
print ("You have entered a total of " + str(count_of_a) + " a, before introducing .")

# Exercise 11: Write a program that reads any two numbers n and m. The program
# must print all the numbers between n and m, including themselves,
# indicating, for each number if it?s even or odd.

n = int(raw_input("Enter the lower number: "))
m = int(raw_input("Enter the upper number: "))

for i in range(n,m+1):
    print (i)
    if i%2 == 0:
        print("Even number")
    else:
        print("Odd number")


# Exercise 12: Write a program that reads numbers one by one until the user
# enters a negative number. Then, the program must display the average of all
# the numbers.

number = int(raw_input("Enter a number"))
average = 0
counter = 0
while number >= 0:
    average = average + number
    number = int(raw_input("Enter a number"))
    counter = counter + 1
print ((str(average/counter) + " is the average"))

# Exercise 13: Write a program that reads numbers, a single number at a time,
# until the user enters a negative number. Then, the program must display the
# average of all the even numbers and the average of all odd numbers.

number = int(raw_input("Enter a number"))
average_odd_numbers = 0
average_even_numbers = 0
counter_odd_numbers = 0
counter_even_numbers = 0
while number >= 0:
    if number%2 == 0:
        average_even_numbers = average_even_numbers + number
        counter_even_numbers = counter_even_numbers + 1
        number = int(raw_input("Enter a number"))
    else:
        average_odd_numbers = average_odd_numbers + number
        counter_odd_numbers = counter_odd_numbers + 1
        number = int(raw_input("Enter a number"))
print ("The average of the odd numbers is " + str(average_odd_numbers/counter_odd_numbers))
print ("The average of the even numbers is " + str(average_even_numbers/counter_even_numbers))

# Exercise 14: Write a program that reads two integers a ? 0 and b ? 0 and
# calculates the product using successive additions.

a = int(raw_input("Enter the first value: "))
b = int(raw_input("Enter the second value: "))
result = 0
n = 0
while a < 0 or b < 0:
    if a < 0:
        print ("Reenter the first value since it's not possitive")
        a = int(raw_input("Enter the first value: "))
    else:
        print ("Reenter the second value since it's not possitive")
        b = int(raw_input("Enter the second value: "))
while n!=b:
    result = result + a
    n = n + 1
print (result)

# Exercise 15: Write a program that reads two integers a ? 0 and b ? 0 and
# calculates the quotient and remainder of a/b using successive substractions.

a = int(raw_input("Enter the first value: "))
b = int(raw_input("Enter the second value: "))
quotient = 0
remainder = 0
while a < 0 or b < 0:
    if a < 0:
        print ("Reenter the first value since it's not possitive")
        a = int(raw_input("Enter the first value: "))
    else:
        print ("Reenter the second value since it's not possitive")
        b = int(raw_input("Enter the second value: "))
while a > 0:
    a = a - b
    quotient = quotient + 1
remainder = a
print ("The quotient is " + str(quotient) + ", while the remainder is " + str(remainder))

# Exercise 16: Write a program that reads an integer number (n > 0) and prints
# its digits right to left.
# Sample output for n = 432 inverted_n = 234 ?
# Help: You can use division and modulus operations to obtain the digits of the
# number. To obtain the inverted number, consider that, for instance:
# 432 = 400 + 30 + 2 = 4 * 10 * 10 + 3 * 10 + 2

n = int(raw_input("Enter the number: "))
reverse = 0
while n <= 0:
    print ("Reenter the number since it's not possitive")
    n = int(raw_input("Enter the number: "))
while n%10 !=0:
    a = (n % 10)
    reverse = (reverse*10) + a
    n = n/10
print(reverse)

# Exercise 17: Write a program that reads an integer n >= 0 and counts the
# number of figures in the number.
# Examples:
# n = 482 ? The number of figures is 3
# n = 0 ? The number of figures is 1

n = int(raw_input("Enter the number: "))
counter = 0
while n <= 0:
    print ("Reenter the number since it's not possitive")
while n%10 != 0:
    n = n/10
    counter = counter + 1
print (counter)

# Exercise 18: Write a program that reads a number n> 0 and prints all
# its divisors.

n = int(raw_input("Enter the number: "))
while n <= 0:
    print ("Reenter the number since it's not possitive")
for i in range(1, n+1):
    if ((n % i) == 0):
        print(i)

# Exercise 19: Write a program that reads a number n> 0 and prints whether
# that number is, or not, a perfect number. An integer is said to be a perfect
# number if the sum of its divisors, including 1 (but not the number itself),
# is equal to the number. Examples:
# 6 is a perfect number because 1 + 2 + 3 = 6

divisor_sum = 0
n = int(raw_input("Enter the number: "))
while n <= 0:
    print ("Reenter the number since it's not possitive")
for i in range(1, n):
    if ((n % 1) == 0):
        divisor_sum = divisor_sum + i
if divisor_sum == n:
    print (n + "is a perfect number")
else:
    print (n + "is not a perfect number")

# Exercise 20: An Armstrong number has an interesting property that the sum
# of cubes of its digits is equal to the number itself
# Write a program that prints all three-digit Amstrong numbers.

sum_for_armstrong = 0
n = int(raw_input("Enter the number: "))
while n <= 0:
    print ("Reenter the number since it's not possitive")
while n%10 != 0:
    digit = n % 10
    sum_for_armstrong = sum_for_armstrong + digit**3
    n = n/10
if sum_for_armstrong == n:
        print ("It is an Armstrong number")
else:
        print ("It is not an Armstrong number")























