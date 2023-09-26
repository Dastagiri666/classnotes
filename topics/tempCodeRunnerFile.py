list_1 = input()
list_2 = []
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)