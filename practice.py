x = 2
y = 1
z = 3
n = 3



res = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(res)

#SWAP CASE
#return "".join([i.upper() if i == i.lower() else i.lower() for i in s])

#splitting a string into an array, and joining it back to a string:
helloarr = "hello world".split(" ")
hellostring ="-".join(helloarr)
print(hellostring)