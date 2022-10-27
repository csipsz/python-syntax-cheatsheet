#conditional == equal, != not equal 
#assignment =
print('a' > 'Z') #=> True
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