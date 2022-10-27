#FUNCTIONS 

def func():
    print('Run')
    def callback():
        print('Running callback')
    callback()

func() #=> Run
       #=> Running callback

#you can add optional/default parameters
def func2(x,y, z=None):
    print(x ** y)
    return x ** y, x * y #=> multiple values are returned in a tuple

print(func2(5,2)) #=> prints the return value 

#separate the return values into variables from tuple
#this works but you call the function twice
r1 = func2(2,3)[0]
r2 = func2(2,3)[1]
#only calls the function once
r1, r2 = func2(2,3)
print(r1, r2)



def func(x):
    def callback():
        print(x)

    return callback 

print(func(7)) #=> <function func.<locals>.callback at 0x7fd7314d2d30>
func(7)() #=> 7

x = func(4)
x()

#unpack operator
x = [1,2,3,4,5,6,7]
print(*x) #unpacks and passes in as arguments

def print_pairs(x,y):
    print(x,y)

pairs = [(2,4), (6,8)]

for pair in pairs:
    print_pairs(*pair)

#with dicts: 
print_pairs(**{'x': 2, 'y' : 9})

#args, kwargs - arguments, keyword arguments
def func(*args, **kwargs):
    print(args, kwargs) #=> (1, 2, 3, 4) {'is_loggged': False, 'float': 3.14}
    print(*args) #=> 1, 2, 3, 4
   # print(**kwargs) #=> 'is_loggged' is an invalid keyword argument for print()

func(1,2,3,4,is_loggged=False, float=3.14)
