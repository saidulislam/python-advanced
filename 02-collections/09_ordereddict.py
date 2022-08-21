# regular dictionary
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
print (d)

# to order, you can do something like the following
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
keys = d.keys()
print (keys)

keys = sorted(keys)
print (keys)

for key in keys:
    print (key, d[key])
    
# ordered dictionary
from collections import OrderedDict
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))
print (new_d)

for key in new_d:
    print (key, new_d[key])
    
# you can also do reverse iteration
from collections import OrderedDict
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))
print(new_d)

for key in new_d:
    key, new_d[key]
for key in reversed(new_d):
    print (key, new_d[key])