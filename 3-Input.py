#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UO269412
#
# Created:     09/10/2018
# Copyright:   (c) UO269412 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Exercise 1
# Write a program (in Python) to do the following:
# Prompt the user to enter the name and two marks of a student
name = raw_input ("What is your name?")
first_mark = raw_input ("What was your mark in the first exam?")
second_mark = raw_input ("What was your mark in the second exam?")
# Calculate the average mark of this student
average_mark =((int(first_mark) + int(second_mark))/2)
# Store in a variable the Boolean value “true” if the average is greater or
# equal to 5 Otherwise, store “False”
greater_than_five = average_mark >= 5


# Exercise 2
#Add to the previous program the instructions needed to print the average mark
# as follows:
# The average mark of Lourdes is 3.25
# Pass the subject: False

name = raw_input ("What is your name?")
first_mark = raw_input ("What was your mark in the first exam?")
second_mark = raw_input ("What was your mark in the second exam?")
average_mark =((int(first_mark) + int(second_mark))/2)
passed = greater_than_five = average_mark >= 5

print ("The average mark of " + str(name) + " is " + str(average_mark))
print ("Pass the subject: " + str(passed))

# Exercise 3
# Change the previous print instruction to use the format operator

name = raw_input ("What is your name?")
first_mark = raw_input ("What was your mark in the first exam?")
second_mark = raw_input ("What was your mark in the second exam?")
average_mark =((int(first_mark) + int(second_mark))/2)
passed = greater_than_five = average_mark >= 5

print 'The average mark of {0} is {1}'.format(name, average_mark)
print 'Pass the subject: {0}'.format(passed)

# Exercise 4
# Write a program to prompt the user to enter the radio of a circumference
# and then calculate its area. The result must be written in the screen
# using the format operator as in the following output:
# The area of a circumference with radio 4.00 is 50.2656
# (2 decimals mus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        t be printed for the radio must and 4 for the area)

radio = float(raw_input ("Enter the radio of the cirumference: "))
import math
area = math.pi*radio**2
print area
#print ("The area of a circumference with radio " + str(radio) + " is " + str(area))
print "The area of a circumference with radio {0:.2f} is {1:.4f}".format(radio, area)

# Exercise 5
# Write a program that prompts the user to enter a distance (in meters)
# and print the equivalent distance in inches, feet, yards, …

distance_meters = float(raw_input ("Enter the distance you want to know the equivalent of: "))
distance_inches = distance_meters * 39.3701
distance_feet = distance_meters * 3.28084
distance_yards = distance_meters * 1.09361

print 'The distance {0}m you have entered is equivalent to {1} inches, {2} feet and {3} yards'. format(distance_meters, distance_inches, distance_feet, distance_yards)
