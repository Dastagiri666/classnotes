#tuple topics
#1 indexing and slicing
#2 length
#3 max and min
#4 packing and unpacking

#1 indexing and slicing
x = input().split()
y = list(x)
print(tuple(y[0:2]))

#2 length
x = input().split()
x[1] = "teja"
y = tuple(x)
print(y)

x = tuple(input().split())
print(x)

#3 max and min
x = tuple(input().split())
print(max(x))

x = tuple(input().split())
print(min(x))

#4 packing and unpacking
room = tuple(input().split())
print(room)
r1,r2,*r3,r4 = room
print(r1)
print(r2)
print(r3)
print(r4)

