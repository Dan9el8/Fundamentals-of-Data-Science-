# Lists are contained in square brackets and can contain several values of different data types
list = [1, 2, 'ten', True]

#List have several useful methods available in python such as concatenation, repetition, length, appending, sorting, indexing etc.
#Concatenation
[1,2,3,4,5] + [4,5]

#repetition
[1,2,3,] * 2

#Length
len(list)

#appending
list.append(32)
print(list)

#sorting
list.sort()
sorted(list)

list.sort(reverse=True)

#Tuples
#tuples are similar to list but cannot be changed once it is created this is called immutability

tuple = (2,3,4)

#list can be converted to tuples using tuple function
tuple(list)

#sets
#Set follow the mathematica definition which is a group of unique values, it can be created using curly brackets or the set() function
set(list)
set = {2.3,3,5,9}

#we can combine two sets using union
set_1 = {1,2,3,4}
set_2 = {5,3,2,2}
set_1.union(set_2)
set_1 | set_2

#Dictionaries
#Dictionaries are similar to sets because they have a unique set of keys but they also contain elements with key-value pairs
dict = {'book': 1, 'magazine': 2, 'articles': 7}

#We can get values of a key using
dict['book']

