#LAMBDA is a one line anonymous function
x = lambda x: x - 3  #not how is used, just shows functionality
print(x(9))

#map  and filter

x = [1,2,3,4,5]
mp = map(lambda i: i - 2, x) #=> map returns a map object
print(list(mp))

ft = filter(lambda i: i % 2 == 0, x) 
print(list(ft))

def func_for_map(i):
    i = str(i) + " Yes"
    return i
#you can add a function as an argument, or write inline a lambda 
print(list(map(func_for_map, x)))

#F strings 
x = f'hello {-1 or -6} {not False} {var1}'
print(x)
