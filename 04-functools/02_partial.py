from functools import partial
def add(x, y):
    return x + y

p_add = partial(add, 2) # you are passing 1 param first
# then you wait
print(p_add(4)) # then you pass the 2nd param