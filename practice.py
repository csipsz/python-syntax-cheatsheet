import textwrap

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

#mutate strings: 
# string = string[:5] + "k" + string[6:]

#control the max width of a line with textwrap module 
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

wrap('helloworld', 3)

#counting occurrences of substring
def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)):
        if string[i:len(sub_string) + i] == sub_string:
            counter += 1
        i += 1
    return counter
#counting occurrences of substring using find instead of iterating through every character
    # def count_substring(string, sub_string):
    # count = 0
    # while string.find(sub_string) != -1:
    #     i, count = string.find(sub_string), count+1
    #     string = string[i+1:]
    # return count
#sum can count boolean values
print(sum([True, False, False, False, True, True]))
#with comprehension:
#return sum([string[i:].startswith(sub_string) for i in range(len(string))])
#sum can count boolean values
print(sum([True, False, False, False, True, True]))


import itertools
def countPairs(arr):
    result = 0
    bitands = list(itertools.combinations(arr, 2))
    bins = []
    for i in bitands:
        x, y = i
        bins.append(x & y)     
    for i in bins: 
        if str(i).count('1') == 1:
            result += 1 
    return result
    