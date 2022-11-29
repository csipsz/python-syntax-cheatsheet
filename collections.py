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

    