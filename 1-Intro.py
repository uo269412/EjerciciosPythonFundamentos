#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UO269412
#
# Created:     02/10/2018
# Copyright:   (c) UO269412 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Exercise 1 : Write a program that contains a comemnt and prints
# "Hello, world!"

print ("Hello, world!")             #Prints Hello, world!

# Exercise 2: In the Python interpreter, create a variable called a and assing
# to it the value 3. Now, create a second variable b and assign to it the
# expression a +5

a = 3                               # Assigns a value to a
b = a + 5                           # Assigns a value to b

# Exercise 3: What is the value of b?

print(b)                            # Prints the b value

# Exercise 4: Change the value of the variable a, setting it to 7. Then, what
# is the value of b? Why?

a = 7                               # Assigns a value to a
print (b)                           # Prints the b value

# b doesn't change because it remains on the memory.

# Exercise 5: What is the type of a and b?

print(type(a))                      # Prints the a type
print(type(b))                      # Prints the b type

# Exercise 6: Now, assign to a the value 5.0 and update b by setting b = a + 5
# again. What is the value of b now What is the type?

a = 5.0                             # Assigns a value to a
b = a + 5                           # Assigns a value to b
print(b)                            # Prints the b value

# Now, the b value changed as well, and it changed its type to float.

# Exercise 7: Write an expression to calculate the remainder of 500 divided
# by 7. Check that the result is 3.

print (500%7)

# Exercise 8: Write a program that prins a line with 80 asterisks.

print("*" * 80)

# Exercise 9: Search on Internet the formula to convert Farenheit to Celsius.
# Then, calculate how many Celsisus degress 45ºF are, with 3 decimals.
# The answer is 7.222

a = (45 - 32)*(5/float(9))
print(round(a,3))