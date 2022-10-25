import datetime
#march_19_2022 = datetime.date(2022, 3)
#print(march_19_2022) #=> TypeError: function missing required argument 'day' (pos 3)
march_19_2022 = datetime.date(2022, 3, 19)
print(march_19_2022) #=> 2022-03-19

time_13_48min_5sec = datetime.time(13, 48, 5) #=> 13:48:05
timestamp = datetime.datetime(2022, 3, 19, 13, 48, 5) #=> #2022-03-19 13:48:05

# from matplotlib import pyplot as plt
# x = plt.plot(2, 3)
# print(x)
import calendar as c
print(c.month_name[1])

#3 ways: import module, from module import functions, or from module import *. 
# from module import * is discouraged, as it can lead to a cluttered local namespace

# import module
# module.function()

# from module import function
# function()

# from module import *
# function()
# random.randint() and random.choice()


# import filename, provided that it is in the current directory
import other_file
other_file.lets_print("It's going to be a lovely day!")

#############################FILES#######################################

with open('other_file.py') as file_object:
    print(file_object) #=> <_io.TextIOWrapper name='other_file.py' mode='r' encoding='UTF-8'>
    print(file_object.readline()) #=> prints 1st line
    print(file_object.readline()) #=> 2nd line

#parsinng json to a dicionary

import json
with open('json.json') as json_file:
  python_dict = json.load(json_file)
  
print(python_dict.get("47915851546270")) #=> {'name': 'Evan Cooper', 'age': 45, 'position': 'Corporate investment banker'}


#'a' for append. so it doesn't overwrite a file. It creates a new file if it doesn't exist
with open('shopping.txt', 'a') as shop:
  shop.write('Tomatoes\nmilk\noats')

with open('shopping.txt','w') as shop:  #overwrites
  shop.write('bread\nfish\napples\nhoney')

with open('shopping.txt') as shop:
  file_data = shop.readlines()
  text_data = shop.read()
print(file_data) #=> returns a list of strings
print(text_data) #=> reads the whole file

for line in file_data:
  print(line)


###############################################

import csv

with open('companies.csv', 'w') as csvfile:
  fieldnames = ['name', 'type']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'name': 'Kroger', 'type': 'shopping'})
  writer.writerow({'name': 'Amazon', 'type': 'online shopping'})