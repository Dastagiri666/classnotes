#1.write a python program to merge two lists.
variable_1 = (input().split())
variable_2 = (input().split())
variable_3 = variable_1 + variable_2
print(variable_3)

#another method
variable_1 = input().split()
variable_2 = input().split()
variable_1.extend(variable_2)
print(variable_1)

#2.write a python program to find the sum of list elements.
list_1 = list(map(int,input().split()))
print(list_1)
print("sum of list_1:",sum(list_1))


#3.write a python program to print even and odd numbers seperatly in list.
list_1 = list(map(int,input().split()))
even = []
odd = []
for i in list_1:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#another method
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print(even)
print(odd)

#4.write a python program to delete element of given index in list.
list_1 = input().split()
list_1.pop(4)
print(list_1)

#another mothod
list_1 = input().split()
del list_1[4]
print(list_1)

#5.write a python program to delete given elemet from the list 
list_1 = input().split()
list_1.remove("4")
print(list_1)

#6.write a python program to insert an elemet  at given index location
list_1 = input().split()
list_1.insert(2,"giri")
print(list_1)

#7.write a python program to check the sizes of given two lists are same
list_1 =input().split()
list_2 = input().split()
print(len(list_1) == len(list_2))

#another method
list_1 =input().split()
list_2 = input().split()
if ((len(list_1) == len(list_2))):
    print(True)
else:
    print(False)


#8.Write a Python function that takes two lists and returns True if they have at least one common member
list_1 =input().split()
list_2 = input().split()
for i in list_1:
    for j in list_2:
        b = i==j
        if b:
            print("True")

        else:
            print("False")   
            

#Write a Python program to remove a specified column from a given nested list
list_1 =[]
n =int(input("enter a size"))
for i in range (n):
    list_2 =[]
    for j in range(n):
        na = int(input("enter values:"))
        list_2.append(na) 
    list_1.append(list_2)
a = 0 
for i in list_1: 
    i.pop(a)
print(list_1)

#9. Write a Python program to convert a list of multiple integers into a single integer.
list_1 = input().split()
for i in list_1:
    print(i,end = "")

#10.Write a Python program to remove duplicates from a list
list_1 = input()
list_2 = []
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)