#SLICE - for collections (arrays, tuples) and strings 
x = [3,4,5,7,9,10,17]
#x[start:stop:step]
sliced = x[0:4:2]
x[2:] #starts at 2, stops at end
x[:2] #starts at beginning, stops at 2
x[::-1] #reverse the sting/array
print("hello world"[::-1]) #=> dlrow olleh