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