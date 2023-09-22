
# Write a program to remove a given character from string

string_1 = "Marolix"
print(string_1.replace("a",""))

# Write a program to check a string is polindrome or not
 
string_1 = "noon"
string_2 = ""
for i in string_1:
     string_2 = i + string_2 
if (string_1 == string_2):
    print("polindrom")
else:
    print("not polindrom")

# charecter is vowel or cosonent
vowels = ("a","e","i","o","u")
string_1 = "q"
if string_1 in vowels:
    print("vowels")
else:
    print("consonent")     

#replace srting space with given charecter
string_1 = "Marolix"
print(string_1.replace("a","  "))

#to count alphabets, digits and special charecters
string_1 = "nuyw#5736@$kjd"
alphabets = 0
digits = 0
special_charecter = 0
for i in string_1:
    if i.isalpha():
        alphabets += 1
    elif i.isdigit():
        digits += 1
    else:
        special_charecter += 1
print(alphabets)
print(digits)
print(special_charecter)


#to remove all the blank spaces
string_1 = ("Marolix Technology")
print(string_1.replace(" ",""))

#find sum of integers in a string
string_1 = "g2ir5i9"
digits = 0
for i in string_1:
    if i.isdigit():
        i = int(i)
        digits += i
print(digits)

#remove repeated char in a string
string_1 = " Hacker rank"
string_2 = ""
for i in string_1:
    if i not in string_2:
        string_2 = string_2 + i
print(string_2) 

#count accurence of a given string
string_1 = "marolix technology"
print(string_1.count("l"))

#check string is anagram or not
string_1 = "dastagiri"
string_2 = "gridaisat"
if(sorted(string_1) == sorted(string_2)):
    print("anagram")
else:
    print("not anagram") 



                

       
