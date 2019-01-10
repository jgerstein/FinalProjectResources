import random

class Thing:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    __repr__ = __str__

things = [Thing(random.randint(-100, 100)) for n in range(20)]

# # Good idea but confuses Python
# print(things)
# for thing in things:
#     if thing.value < 0:
#         things.remove(thing)

print(things)
temp_things = []
for thing in things:
    if not thing.value < 0:
        temp_things.append(thing)

print(temp_things) # This now contains all the positive values

# replace things with temp_things
things[:] = temp_things
print(things)