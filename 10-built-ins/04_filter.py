# The filter built-in function will take a function and an iterable and return 
# an iterator for those elements within the iterable for which the passed in 
# function returns True. That statement sounds a bit confusing to read.

def less_than_ten(x):
    return x < 10

my_list = [2, 4, 6, 11, 30, 5]

for item in filter(less_than_ten, my_list):
    print(item)

print(list(filter(less_than_ten, my_list)))