# 1.map()

#method:1
def square(x):
    return x*x
l = [1,2,3,4,5]
l1 = list(map(square,l))
print(l1)

#method:2
def myfunc(a):
  return len(a)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
print(list(x))                             #convert the map into a list, for readability:

#method:3
my_list = [2.6743,3.63526,4.2325,5.9687967,6.3265,7.6988,8.232,9.6907]
updated_list = map(round, my_list)
print(updated_list)
print(list(updated_list))

# 2.reduce()

#method:1
from functools import reduce 

nums = [1, 2, 3, 4]
ans = reduce(lambda x, y: x + y, nums)
print(ans) 

#method:2
from functools import reduce
# pre-defined function to calculate minimum
def mini(a, b):
    return a if a < b else b
# pre-defined function to calculate maximum
def maxi(a, b):
    return a if a > b else b
nums = [3, 5, 2, 4, 7, 1]
# passing both functions in the reduce along with nums as iterable
print('The minimum in the given list is', reduce(mini, nums))
print('The maximum in the given list is', reduce(maxi, nums))

#method:3
from functools import reduce
# creating a function to check if both arguments are True or not
def is_true(a, b):
   return bool(a and b)
print(reduce(is_true, [1, 1, 1, 1, 1]))
print(reduce(is_true, [1, 1, 1, 1, 0]))

# 3.filter

#method:1
def find_even(x):
    if x%2 == 0:
        return True
    else:
        return False
l = [1,2,3,4,5,6,7,8,9,10]
l1 = filter(find_even, l)
print(list(l1))

#method:2
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False
filtered_vowels = filter(filter_vowels, letters)
# converting to tuple
vowels = tuple(filtered_vowels)
print(vowels)

#method:3
numbers = [1, 2, 3, 4, 5, 6, 7]
# the lambda function returns True for even numbers 
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)
# converting to list
even_numbers = list(even_numbers_iterator)
print(even_numbers)

# 4.lambda()

# method:1
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

# method:2
# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)
# lambda call
greet_user('giri')

# method:3
x = lambda a: a+10
print(x(5))

# 5.recursive()
def recursive_function(x):
   if x == 1:
      return 1
   else:
      return x*recursive_function(x-1)
num = 4
print(recursive_function(num))






