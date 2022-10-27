#Local and global scope 

var1 = "global_variable"

def func(fruit):
    var1 = fruit 

print(var1) #=> global_variable
func('grape')
print(var1) #=> global_variable

#////////////////////////////////////////

var1 = "global_variable"

def func(fruit):
    global var1
    var1 = fruit 

print(var1) #=> global_variable
func('grape')
print(var1) #=> grape