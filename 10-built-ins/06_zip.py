# The zip built-in takes a series of iterables and aggregates the elements from each of them.

keys = ['x', 'y', 'z']
values = [5, 6, 7]
print(zip(keys, values))

print(list(zip(keys, values)))
print(dict(zip(keys, values)))
