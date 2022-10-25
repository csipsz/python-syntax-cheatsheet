import json
from faker import Faker
from random import randint
#fake = Faker('hu_HU')
fake = Faker('en_US')
for i in range(5):
    my_dict = { randint(0, 100000000000000) : {"name": fake.name(), "age": randint(16, 80), "position": fake.job() } }
    print(my_dict)

json_object = json.dumps(my_dict, indent=4) 
print(json_object)
