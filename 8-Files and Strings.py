#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      UO269412
#
# Created:     04/12/2018
# Copyright:   (c) UO269412 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Exercise 1:

# Function lastChars, receiving two strings and returning a string
# with the first symbol of the former and the last one from the latter. If
# either string is length 0, use ?@? for its missing char.

def lastChars(first_string , second_string):
    if(len(first_string) == 0):
        a = "@"
    else:
        a= first_string[0]
    if(len(second_string) == 0):
        a = a + "@"
    else:
        a = a + second_string(len(second_string)-1)
    return a

first = str(raw_input("Enter the first string: "))
second = str(raw_input("Enter the second string: "))
result = lastChars(first, second)
print result

# Function makeTags the web is built with HTML strings like "<i>Yay</i>"
# which draws Yay as italic text. In this example, the "i" tag makes <i> and
# </i> which surround the word "Yay". Given tag and word strings,
# create the HTML string with tags around the word, e.g. "<i>Yay</i>".

def makeTags(symbol, italic):
    return ("<" + str(symbol) + ">" + str(italic) + "</" + str(symbol) + ">")

symbol = str(raw_input("Enter the symbol: "))
italic = str(raw_input("Enter the italic: "))

result = makeTags(symbol,italic)
print result

# Function rotateleft(string, pos) given a string, return a "rotated left x"
# version where the first x chars are moved to the end. The string length will
# be at least 2. or an error will raise.

def rotateleft(string, pos):
    a = ""
    for i in range (pos, len(string)):
        a += string[i]
    j = 0
    while j<pos:
        a += string[j]
        j += 1
    return a

print rotateleft("Hello", 2)
print rotateleftleft("java", 3)
rotateleft("Hi",2)

# Exercise 4: Write a function that implements a substitution cipher. In a
# substitution cipher one letter is substituted for another to garble the
# message. For example A -> Q, B -> T, C -> G etc. your function should take two
# parameters, the message you want to encrypt, and a string that represents
# the mapping of the 26 letters in the alphabet. Your function should return a
# string that is the encrypted version of the message. For this exercise,
# limit the strings to include only alphabetical symbols and white spaces.

def substitution_cipher(message,mapping):
    a = ""
    for i in range(len(message)):
        if message[i].upper() == "A":
            a += map[16]
        elif message[i].upper() == "B":
            a += map[19]
        elif message[i].upper() == "C":
            a += map[6]
        else:
            a += message[i]
    return a
message = "HOLA"
map = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = substitution_cipher(message, map)
print result


# Write a function that decrypts the message from the previous exercise. It
# should also take two parameters. The encrypted message, and the mixed up
# alphabet. The function should return a string that is the same as the
# original unencrypted message. For this exercise, limit the strings to include
# only alphabetical symbols and white spaces.

def decrypt(message,map):
    a = ""
    for i in range(len(message)):
        if message[i].upper() == map[16]:
            a += "A"
        elif message[i].upper() == map[19]:
            a += "B"
        elif message[i].upper() == map[6]:
            a += "C"
        else:
            a += message[i]
    return a

message = "HOLA"
map = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = substitution_cipher(message, map)
decryption = decrypt(result,map)
print decryption

# Write a function called rot13 that uses the Caesar cipher to encrypt a
# message. The Caesar cipher works like a substitution cipher but each character
#  is replaced by the character 13 characters to ?its right? in the alphabet.
# So for example the letter a becomes the letter n. If a letter is past the
# middle of the alphabet then the counting wraps around to the letter a again,
# so n becomes a, o becomes b and so on. Hint: Whenever you talk about
# things wrapping around its a good idea to think of the arithmetic remainder
# from the integer division.

def rot13(message, map):
    a = ""
    for i in range(len(message)):
        if map.index(message[i])<13:
            a+= map[map.index(message[i]) + 13]
        else:
            a+= map[map.index(message[i]) - 13]
    return a

message = "HOLA"
map = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = rot13(message,map)
print result

# Using the methods count and lower, and the operator in, write a function
# called count_vowels for counting the occurrences of each vowel in a given
# text. The function should return a list with the vowel?s occurrences,
# from ?a? to ?u?.

def count_vowels(text):
    list = []
    list.append(text.count("a"))
    list.append(text.count("e"))
    list.append(text.count("i"))
    list.append(text.count("o"))
    list.append(text.count("u"))
    return list

example = "hola que tal"
result = count_vowels(example)
print result

# Now, let?s do the same but for all the letters from ?a? to ?z?. Therefore,
# write a function called count_letters that receives a string and returns a
# list with the occurrences of each letter from ?a? to ?z?

def count_letters(text):
    map = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    list = []
    for i in range(len(map)):
        list.append(text.upper().count(map[i]))
    return list

example = "hola que tal"
result = count_letters(example)
print result

# Write the function metamorphosis for automatically converting from a string
# to any valid data type among the following:
# ? integer: just containing digits plus leading and ending spaces,
# ? bool: True or False plus leading and ending spaces,
# ? float: digits+dot+digits format, allowing ? 23.4 ?, ? .234 ? and ? 234.? as valid floats,
# ? str: the remaining cases it is just a string!

def metamorphosis(a):
    no_spaces = a.strip()
    if no_spaces == "True" or no_spaces == "False":
        print "boolean"
        result = bool(no_spaces)
    elif " " in no_spaces:
        print "string"
        result = no_spaces
    elif "." in no_spaces:
        print "float"
        result = float(no_spaces)
    else:
        print "int"
        result = int(no_spaces)
    return result


# Write a function randomValue for generating a list of 100 random values within
# the interval defined by [lowerBound, upperBound], both values are given to the function.

import random
def randomValue(lowerBound, upperBound):
    f = open ("C:\Users\javie\Desktop\FI\Lab\python\singleData.txt", 'w')
    m = open ("C:\Users\javie\Desktop\FI\Lab\python\dataset.csv", 'w')
    for i in range(101):
        f.write(str((random.randint(0,10)*0.1)*(random.randint(0,250)*0.01)) + "\n")
        a = str((random.randint(0,10)*0.1)*(random.randint(0,250)*0.01))
        b = str((random.randint(0,10)*0.1)*(random.randint(-100,100)*0.01))
        c = str((random.randint(0,10)*0.1)*(random.randint(0,100)*0.01))
        d = str((random.randint(0,10)*0.1)*(random.randint(2,450)*0.01))
        m.write(a + "," + b + "," + c + "," + d + "\n")
    f.close()
    m.close()

result = randomValue(2,2)

# Download the file students.txt. It contains a list of all the students
# enrolled in a subject. If you take a look at the file, opening it with
# Notepad, you?ll see that it contains one name per line, first the last name
# and then, separated by a comma, the name. They are in random order.
# Then, do the following exercises with this file.

# Write a python function to find out the total number of students.

def total_number():
    f = open ("C:\Users\javie\Desktop\FI\Lab\python\students.txt", 'r')
    list = f.readlines()
    f.close()
    b = ",".join(list)
    counter = b.count("\n")
    return counter

result = total_number()
print result

# Write a function that receives two parameters: a line read from the file and
# the last name of a person. This function should return True if the last name
# (one of them for Spanish students) of the person match the given name

import random
f = open ("C:\Users\javie\Desktop\FI\Lab\python\students.txt", 'r')
counter = random.randint(0,899)
found = False
for line in f:
    if found != True:
        if counter>0:
            counter -=1
        else:
            random_line = line
            found = True

print random_line
f.close()

def match_lastName(line, name):
    list_line = line.split(",")
    list_line.pop(1)
    list_line = " ".join(list_line)
    return name in list_line

a = match_lastName("Tajes Martinez, Lourdes", "Tajes")
b = match_lastName("Tajes Martinez, Lourdes", "Vidal")
c = match_lastName("Tajes Martinez, Lourdes", "Lourdes")
print a,b,c

#  Using the previous function find out what percentage of students have
# Fernandez as one of their two last names


counter = 0
students = total_number()
f = open ("C:\Users\javie\Desktop\FI\Lab\python\students.txt", 'r')
for line in f:
     if match_lastName(line,"Fernandez"):
        counter = counter +1
print counter,students
