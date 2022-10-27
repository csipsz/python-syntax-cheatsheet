#raise Exception('Wrong value') #=>  raise Exception('Wrong value')
                                #Exception: Wrong value
#raise FileNotFoundError('404') #=> won't get to here, already raised exception

try:
    False / 0
except ArithmeticError as e:
    print(e)
finally:
    print("Past the exception")
