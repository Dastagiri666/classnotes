def calculator(x,y):
    m = int(input("enter a num:"))
    if m == 1:
        return(x+y)
    elif m == 2:
        return(x - y)
    elif m == 3:
        return(x * y)
    elif m == 4:
        if y != 0:
            return( x / y)
        else:
            return("Cannot divide by zero")
    else:
        return("you entered value is invalid")

a = int(input())
b = int(input())
print (calculator (a,b))