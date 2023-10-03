# 1.Write a Python program to unpack a tuple into several variables.
variable_1 = tuple(input().split())
print(variable_1)
(room_1,room_2,room_3,room_4,room_5) = variable_1
print(room_1)
print(room_2)
print(room_3)
print(room_4)
print(room_5)


#2.Write a Python program to add an item to a tuple.
variable_1 = tuple(input().split())
variable_2 = tuple(input().split())
print(variable_1 + variable_2)


# 3.Write a Python program to convert a tuple to a string.
# Ex:tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
variable_1 = tuple(input().split())
variable_1 = "".join(variable_1)
print(variable_1)

#4.Write a Python program to get the specified element from the last element of a tuple.
variable_1 = tuple(input().split())
print(variable_1[-1])

#method 2
variable_1 = tuple(input().split())
variable_2 = int(input())
print(variable_1[variable_2])


#5.Write a Python program to add member(s) to a set.
variable_1 = set(input().split())
variable_1.add("nag")
print(variable_1)


#6.Write a Python program to create an intersection of sets.
variable_1 = set(input().split())
variable_2 = set(input().split())
print(variable_1.intersection(variable_2))


#7.Write a Python program to create a union of sets.
variable_1 = set(input().split())
variable_2 = set(input().split())
print(variable_1.union(variable_2))


#8.Write a Python program to create set difference.
variable_1 = set(input().split())
variable_2 = set(input().split())
print(variable_1.difference(variable_2))

#9.Write a Python program to create a symmetric difference.
variable_1 = set(input().split())
variable_2 = set(input().split())
print(variable_1.symmetric_difference(variable_2))


#10.Write a Python program to find the maximum and minimum values in a set.
variable_1 = set(input().split())
print(max(variable_1))
print(min(variable_1))