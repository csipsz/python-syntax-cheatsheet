#DATA TYPES 

#NUMERIC - 1. INTEGER, 2. FLOAT, 3. COMPLEX NUMBER
#DICTIONARY
#BOOLEAN
#SET
#SEQUENCE TYPE - 1. STRING, 2. LIST, 3. TUPLE

#VARIABLE

name = "Tim"
# => hello_world - Python uses snake case (obviously), variables can't start with a digit
print(type(name)) # => <class 'str'>
print(5>10) # => False

print("hello", end="|") # => overwrites the default(every print statement starts at a new line)
print("and welcome!")

# username = input("Please enter username: ") # input will be string, even if int 
# print(type(username))

quote ="""I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.
- William Wordsworth """
print(quote)

#int() float() complex() bool() 
int(5.4) # => 5
bool("Hello") # => True

#COMPLEX NUMBERS 
num = 5 + 3j
print(num)

result = 6 / 3 # => returns a float 
result2 = 10 // 3 #=> floor division
6 ** 3 # => exponent
6 % 5 # => modulo 
"hello" * 7

#ORDER OF OPERATION 
#BRACKETS
#EXPONENTS
#DIVISION
#MULTIPLICATION
#ADDITION
#SUBTRACTION

float_or_int = 5 - 5.0 #=> returns a float when there is a float i the expression

#STRING METHODS

"python".upper()
"python".lower()
"python".capitalize()
"python".count("t")
"python".upper().count("T")

#conditional == equal, != not equal 
#assignment =
print('a' > 'Z')
#ordinal value 
print(ord('a'), ord('Z'))

7.0 == 7 #=> returns True
z = 9
x = 8 
result3 = z < x + 2 # => True
#conditional operators have a lower precedence than arithmetic operators

#chain conditionals - in the order of precedence
# not
# and
# or

print(5 < 4 or not True and True) #=> False 
print(5 < 4 or not True and True or True) #=> True
print(not (True and False)) #=> True

condition = "Totally"
if condition == "Totally":
    print("That's right!")
elif condition == "Maybe":
    print("That could also work!")
else:
    print("Nevermind, then, let's default to the original plan!")

#Collections, lists...
list1 = [7, False, "Hello"]
list1.append(3.14)
list1.extend([1,2,3,4,5,6]) # => concatenates, adds it to the end of the list1
list1.pop() #=> returns removed last element, can take in index as an argument
print(len(list1), len(list1[2]))
list1[2] = "reassigned_new_value"

#lists are mutable - x and y stores a reference to the list1, not a copy of the list1
x = [2, "cats", "are", "better", "than", 1]
y = x
x[0] = 3 
print(x, y) #=> [3, 'cats', 'are', 'better', 'than', 1] for both variables
#to copy a list1
y = x[:]

#...and tuples (which are immutable)
x = (True, False, True, False)
#x[1] = True #=> TypeError: 'tuple' object does not support item assignment
print(x[1])
#can have a list1 of lists and tuples
y = [[], [], (), (1,2,3),[["Hello"], ["Greetings"]]]

#FOR LOOPS

for i in range(10):
    print(i) #=> does not include 10 
#arguments for range(start, stop, step)
# 1 argument start
# 2 arguments start, stop
# 3rd argument is step

for i in [1,2,3,4,5]:
    print("I wanted to say this 5 times")

for i in range(50, 5, -5):
    print(str(i) + " is next")

x = [1,8,3,9,5]
for i, element in enumerate(x):
    print(i, element)

#WHILE LOOPS
i = 0
while i < 20:
    print("adding 5 to " + str(i))
    i += 5 
print("We've reached 20") 

# i += 2
# i -= 2
# i /= 2
# i *= 2

while True:
    print("You don't have to stuck in an infinite loop if you don't want to!")
    break

#SLICE - for collections (arrays, tuples) and strings 
x = [3,4,5,7,9,10,17]
#x[start:stop:step]
sliced = x[0:4:2]
x[2:] #starts at 2, stops at end
x[:2] #starts at beginning, stops at 2
x[::-1] #reverse the sting/array
print("hello world"[::-1]) #=> dlrow olleh

#SETS - fast in lookups, additions or removals
#freuency, order doesn't matter, just the existence of the value 
x = set() #creates empty set
s = { 1,1,1,1,3,3,3,4,4,4,7,7,7,8,8,90 } #set literal
print(s) #=> {1, 3, 4, 7, 8, 90}
s.add(11)
s.remove(1)
print(3 in s) #=> True - very fast computation
s2 = {18,19,50,76}
s.union(s2)
s.difference(s2)
s.intersection(s2) #=> common values in 2 sets

not_s = {} #creates empty dictionary
print(type(set())) #=> <class 'set'>
print(type({})) #=> <class 'dict'>

#DITIONARIES - also very fast, like set
#key can be almost any data type
x = {'key': 4}
print(x['key'])
x['new_value'] = 9
x[8] = 8
x[True] = True
x[2.4] = 'float'
#x[['array']] = 78 #=>TypeError: unhashable type: 'list1'
x[(2,3)] = (2,3,4)
#x[{1,2,3}] = set #=> TypeError: unhashable type: 'set'
print('new_value' in x) #=> True
print(list(x.values()))
del x['key'] #=> deletes the key
print(list(x.keys()))

for key, value in x.items():
    print(key, value, "+")

for whatever in x: #=> still prints the keys. The order of the arguments matter, key and value are not keywords here 
    print(whatever)

#COMPREHENSIONS
x = [x for x in range(10)]
#creates a for loop inside a list
x = [x - 5 for x in range(10)]
x = ["It's only " + str(x) + " AM!" for x in range(10)]
x = [["Hi" for x in range(7)] for x in range(20)]
#=> creates an array of 20 arrays with 7 values in each
#works with dicts too:
x = {i:'even' for i in range(10) if i % 2 == 0}
#=> {0: 'even', 2: 'even', 4: 'even', 6: 'even', 8: 'even'}
#works for sets:
x = {i for i in range(10) if i % 2 == 0} #=> {0, 2, 4, 6, 8}
#works different for tuples - generator object
x = tuple(i for i in range(10) if i % 2 == 0)
print(x)

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










