# The map built-in also takes a function and an iterable and returns 
# an iterator that applies the function to each item in the iterable.

def doubler(x):
    return x*2

my_list = [2, 3, 5, 6, 4, 8]
for item in map(doubler, my_list):
    print(item)

print(list(map(doubler, my_list)))