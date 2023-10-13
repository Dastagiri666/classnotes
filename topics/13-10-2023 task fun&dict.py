#functions

# 1.Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# 2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# 3.Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog".

# 4.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included).

# 5.Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 

# 6.write a function to find sum of given values, pass values has variable number of arguments to function.




# 1.Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
            pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
string_test('The quick Brown Fox')


# 2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_list(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return(x)
print(unique_list([1,2,3,3,3,3,4,5]))


# 3.Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog".
import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
 
print ( ispangram('The quick brown fox jumps over the lazy dog')) 



# 4.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included).
def square():
    x = []
    for i in range(1,10+1):
        x.append(i**2)
        print(x)
square()
    

# 5.Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 
def sum(l):
    x = 0
    for i in l:
        x += i
    return x
print(sum((8, 2, 3, 0, 7)))


# 6.write a function to find sum of given values, pass values has variable number of arguments to function.



# Dictionary

# 1.Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# 2.Write a Python script to check whether a given key already exists in a dictionary.

# 3.Write a Python program to iterate over dictionaries using for loops

# 4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# 5.Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'marolix technology'
# Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}

# 6. Write a Python program to sum all the items in a dictionary.

# 7.Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# 8.Write a Python program to access dictionary key's element by index.
# Expected Output:
# physics
# math
# chemistry

# 9.Write a Python program to remove a key from a dictionary.

# 10.Write a Python script to merge two Python dictionaries.d


# 1.Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
dict = {0:10, 1:20}
print(dict)
dict.update({2:30})
print(dict)

# 2.Write a Python script to check whether a given key already exists in a dictionary.
dict = {0:10, 1:20}
def key(x):
    if x in dict:
        print("key is present in dict")
    else:
        print("key not present in dict")  
key(2)


# 3.Write a Python program to iterate over dictionaries using for loops
d = {1 :'blue', 2 :'green', 3 :'red'} 
for key_colour, value in d.items():
     print(key_colour, 'corresponds to ', d[key_colour]) 


# 4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
#  and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
d=dict()
for x in range(1,15+1):
    d[x]=x**2
print(d)  


# 5.Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'marolix technology'
# Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}
from collections import defaultdict, Counter
str1 = 'marolix technology' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

# 6. Write a Python program to sum all the items in a dictionary.
dict = {"key1": 10, "key2": 20, "key3": 30}
print(sum(dict.values()))


# 7.Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
from collections import Counter
dict_1 = {'a': 100, 'b': 200, 'c':300}
dict_2 = {'a': 300, 'b': 200, 'd':400}
dict_3 = Counter(dict_1) + Counter(dict_2)
print(dict_3)


# 8.Write a Python program to access dictionary key's element by index.
# Expected Output:
# physics
# math
# chemistry
num = {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(num)[0])
print(list(num)[1])
print(list(num)[2])

# 9.Write a Python program to remove a key from a dictionary.
num = {'physics': 80, 'math': 90, 'chemistry': 86}
num.pop("math")
print(num)

# 10.Write a Python script to merge two Python dictionaries.
dict_1 = {'a': 100, 'b': 200, 'c':300}
dict_2 = {'d': 300, 'e': 200, 'f':400}
dict_3 = dict_1.copy()
dict_3.update(dict_2)
print(dict_3)