#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UO269412
#
# Created:     27/11/2018
# Copyright:   (c) UO269412 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

list1=[5,8,10]
list2=[3,2,9,12,4]

# Find out the lenght of each list

print("The length of the first list is " + str(len(list1)))
print("The lenght of the second list is " + str(len(list2)))

# Concatenate

list3 = list1 + list2
print(list3)
print("The lenght of the third list is {0}".format(len(list3)))

# Largest number in both lists

max_in_list1=max(list1)
print("The max number in list1 is {0}".format(max_in_list1))
max_in_list2=max(list2)
print("The max number in list2 is {0}".format(max_in_list2))
max_in_both_lists=max(max_in_list1,max_in_list2)
print("The max number in list3 is {0}".format(max_in_both_lists))

# Write an expression to add the first element of each list
# (must add 5 and 3 to produce 8).

x = (list1[0]+list2[0])
print(x)

# Write an expression to add the last element of each list (10 +4).

y = list1[-1]+list2[-1]
print(y)

# Write a sentence to replace number 8 in list1 with 0.
# Check that the element has changed.

list1[1]=0
print(list1[1])

#  Run the sentence list3 = list2. Then, print list3 to check its content
# (must be 3,2,9,12 and 4)

list3=list2
print(list3)

# Modify list3 so that its first element is 7. Print its content

list3[0]=7
print(list3)

# Now, print list2. The first has changed. This is because, due to the
# assignment list3 = list2, both variables refer to the same list

print(list2)

# Write a loop to print each element in list1

for i in range(len(list1)):
    print list1[i]

# Write a loop to print list2 upside down
# (starting with the last and ending with the first).

for i in range(len(list2)+1):
    print list2[-i]

# Write a function that receives a list and returns the sum of all the elements
# in the list, computed iterating over the list with a loop.
# Then, from the interpreter, create a list and invoke the function passing
# the list as argument. Then, print the resulting value.
#  Compare it with what comes out of sum(list).

def sum_list(my_list):
    sum = 0
    for i in range(len(my_list)):
        sum = sum + my_list[i]
    return sum

example_list=[1,2,3,4,5,6,7,8,9,10]
result = sum_list(example_list)
print(result)
print(sum(example_list))

# Write a function that receives a list and returns the index (position) of the
# largest element of the list. For example, if the argument is the list
# [4, 2, 7, 1, 3] the function should return 2 since the biggest item in the
# list is "7" and it is in position 2 (remember that positions are numbered
# from zero).

def index_returner(my_list):
    max_number=max(my_list)
    for i in range(len(my_list)):
        if my_list[i]==max_number:
            return i

example_list=[4,2,7,1,3]
result=index_returner(example_list)
print("The max number is in position: "+ str(result))

# Write a function that receives a list and CHANGE all negative numbers in the
# list by zero. The function will return an integer indicating how many changes
# you have made.

def list_changer(my_list):
    changes = 0
    for i in range(len(my_list)):
        if my_list[i]<0:
            my_list[i]=0
            changes +=1
    return changes
example_list=[1,2,-1,-4,6]
result=list_changer(example_list)
print("A total of " + str(result)+ " changes were made")

# Write a function that receives a list l and a number n (integer or real, is
# indifferent) as parameters. This function should calculate the value of each
# item in the list to the power of n and add all them, returning
# the result. That is, if the list is composed of elements xi, the result is
# calculated as P xin.

def power_sum(my_list, n):
    sum = 0
    for i in range(len(my_list)):
        sum = sum + (my_list[i]**n)
    return sum
example_list=[1,2,3]
result=power_sum(example_list,1)
print (result)

#  Given a list of ints any length, return a list with the elements
# "rotated left" so 1, 2, 3 yields 2, 3, 1.

def rotated_left(list):
    last_one = list[0]
    for i in range(len(list)-1):
        list[i] = list[i+1]
    list[len(list)-1] = last_one
    return list
example_list = [1,2,3]

result = rotated_left(example_list)
print result

# Given a list of ints, return True if 6 appears as either the first or last
# element in the list. The list will be length 1 or more

def finder6(my_list):
    for i in range(len(my_list)):
        if (i==0 or i==len(my_list)) and (my_list[i]==6):
            return True
        else:
            return False
example_list=(6,1,2,3)
result=finder6(example_list)
print(result)

# Given a list of ints any length, return a new list with the elements in
# reverse order, so 1, 2, 3 becomes 3, 2, 1.

def rotation(my_list):
    rotated_list = []
    for i in range(len(my_list)+1):
        rotated_list.append(my_list[-i])
    rotated_list.pop(0)
    return rotated_list

example_list = [7,2,3,4,5]
result=rotation(example_list)
print(result)

# Return the number of even ints in the given list.

def even_calculator(my_list):
    even_numbers=0
    for i in range(len(my_list)):
        if my_list[i]%2==0:
            even_numbers+=1
    return even_numbers

example_list=(2,1,2,3,4)
result = even_calculator(example_list)
print (result)

# Given a list length 1 or more of ints, return the difference between the
# largest and smallest values in the list. Note: the built-in min(v1, v2)
# and max(v1, v2) functions return the smaller or larger of two values.

def big_diff(list):
    for i in range(len(list)-1):
        max_number = max(list[i],list[i+1])
        min_number = min(list[i],list[i+1])
        result = max_number - min_number
        return result
example_list = [10,3,5,6]
result = big_diff(example_list)
print result

# Return the "centered" average of a list of ints, which we?ll say is the mean
# average of the values, except ignoring the largest and smallest values in the
# list. If there are multiple copies of the smallest value, ignore
# just one copy, and likewise for the largest value. Use int division to produce
# the final average. You may assume that the list is length 3 or more.

def centered_average(list):
    divisor = len(list)-2
    dividend = 0
    for i in range (1, len(list)-1):
        dividend += list[i]
    result = dividend/divisor
    return result

example_list = [1,2,3,4,100]
result = centered_average(example_list)
print result
example_list = [1,1,5,5,10,8,7]
result = centered_average(example_list)
print result
example_list = [-10,-4,-2,-4,-2,0]
result = centered_average(example_list)
print result

# . Consider a list in the way [string, number, string, number, ...] where the
# string are names and the number is the number of children with that name in
# one year. Write a function that receives such a list and returns the most
# popular name.

def popular_name(list):
    biggest_name = 0
    for i in range(1,len(list),2):
        if list[i]> biggest_name:
            biggest_name = list[i]
    most_popular_name = list.index(biggest_name) - 1
    most_popular_name = list[most_popular_name]
    return most_popular_name

example_list = ['ana', 223, 'laura', 204, 'elena',175]
result = popular_name(example_list)
print result







