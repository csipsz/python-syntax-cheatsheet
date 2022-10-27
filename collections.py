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