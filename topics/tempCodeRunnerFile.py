def recursive_function(x):
   if x == 1:
      return 1
   else:
      return x*recursive_function(x-1)
num = 4
print(recursive_function(num))