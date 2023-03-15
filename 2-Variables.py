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

# Exercise 1

C = 30
F = (C*9/5) + 32
print(F)

F = 77
C = (F-32)*5/9
print (C)

#Exercise 2
S_i = 20
a = 9.8
t = 30
S_f = S_i + a*t
print (S_f)
S_i = - a*t + S_f
print(S_i)
a = ((S_i - S_f)/t)
print(a)
t = ((S_i - S_f)/t)
print(t)

#Exercise 3
a = 6
b = 2
c = ((5<a<=30) and (b%2==0))
print (c)
print (type(c))
d = not((5<a<=30) and (b%2==0))
d = (not(5<a<=30) or (b%2!=0))

#Exercise 4
base = 9
height = 5
area = (str((base/height)/2))
area = str(area)
message = "The area of the triangle is" + area
print (message)
base = "5"
height = "7"
area = float(((base/height)/2))
message = "The area of the triangle is" + area
print (message)

#Exercise 5:

year = 2012
if (year%4 == 0 or (year%100 == 0 and year%400 == 0)):
    leapyear = True
else:
    leapyear = False
print (leapyear)


