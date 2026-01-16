random_list = [42, "chai", 3.14, True, "python", 7, None, "debug", 99]
for i,val in enumerate(random_list):
    print(i,val)


from enum import Enum
class color(Enum):
    red=1
    blue=2
    green=3
print(color.blue.name)
print(color.red.value)