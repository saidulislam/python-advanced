from itertools import count
for i in count(10):
    if i > 20: 
        break
    else:
        print(i)

from itertools import count
from itertools import islice
for i in islice(count(10), 5):
    print(i)
    
# cycle (iterable)
from itertools import cycle
count = 0
for item in cycle('XYZ'):
    if count > 7:
        break
    print(item)
    count += 1
    
from itertools import cycle
polys = ['triangle', 'square', 'pentagon', 'rectangle']
iterator = cycle(polys)
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))


# repeat(object)
from itertools import repeat
repeat(5, 5)
repeat(5, 5)

iterator = repeat(5, 5)
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))

