#DATA TYPES 

#NUMERIC - 1. INTEGER, 2. FLOAT, 3. COMPLEX NUMBER
#DICTIONARY
#BOOLEAN
#SET
#SEQUENCE TYPE - 1. STRING, 2. LIST, 3. TUPLE

#VARIABLE

from multiprocessing.resource_sharer import stop
from tracemalloc import start


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
list = [7, False, "Hello"]
list.append(3.14)
list.extend([1,2,3,4,5,6]) # => concatenates, adds it to the end of the list
list.pop() #=> returns removed last element, can take in index as an argument
print(len(list), len(list[2]))
list[2] = "reassigned_new_value"

#lists are mutable - x and y stores a reference to the list, not a copy of the list
x = [2, "cats", "are", "better", "than", 1]
y = x
x[0] = 3 
print(x, y) #=> [3, 'cats', 'are', 'better', 'than', 1] for both variables
#to copy a list
y = x[:]

#...and tuples (which are immutable)
x = (True, False, True, False)
#x[1] = True #=> TypeError: 'tuple' object does not support item assignment
print(x[1])
#can have a list of lists and tuples
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
