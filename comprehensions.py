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