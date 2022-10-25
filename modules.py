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