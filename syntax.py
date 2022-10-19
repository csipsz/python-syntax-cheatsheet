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
