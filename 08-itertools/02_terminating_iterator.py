from itertools import accumulate
print (list(accumulate(range(10))))

# accumulate(iterable)

from itertools import accumulate
import operator
print (list(accumulate(range(1, 5), operator.mul)))

# chain(*iterables)
# The chain iterator will take a series of iterables 
# and basically flatten them down into one long iterable.
from itertools import chain
my_list = ['foo', 'bar']
numbers = list(range(5))
cmd = ['ls', '/some/dir']
my_list = list(chain(['foo', 'bar'], cmd, numbers))

print (my_list)
#['foo', 'bar', 'ls', '/some/dir', 0, 1, 2, 3, 4]

# You could do this to get the same effect
my_list = ['foo', 'bar']
my_list += cmd + numbers
print (my_list)
#['foo', 'bar', 'ls', '/some/dir', 0, 1, 2, 3, 4]

# chain.from_iterable(iterable)
from itertools import chain
numbers = list(range(5))
cmd = ['ls', '/some/dir']

print (list(chain.from_iterable([cmd, numbers])))
#['ls', '/some/dir', 0, 1, 2, 3, 4]

# compress(data, selectors)
from itertools import compress
letters = 'ABCDEFG'
bools = [True, False, True, True, False]
print (list(compress(letters, bools)))
#['A', 'C', 'D']

# dropwhile(predicate, iterable)
from itertools import dropwhile
print (list(dropwhile(lambda x: x<5, [1,4,6,4,1])))
#[6, 4, 1]


# filterfalse(predicate, iterable)
from itertools import filterfalse
def greater_than_five(x):
    return x > 5 

print (list(filterfalse(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10])))
#[1, 2, 3]


# groupby(iterable, key=None)
from itertools import groupby

vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durango'),
            ('Chevrolet', 'Cobalt'), ('Ford', 'F150'),
            ('Dodge', 'Charger'), ('Ford', 'GT')]

sorted_vehicles = sorted(vehicles)

for key, group in groupby(sorted_vehicles, lambda make: make[0]):
    for make, model in group:
        print('{model} is made by {make}'.format(model=model,
                                                 make=make))
    print ("**** END OF GROUP ***\n")


# islice(iterable, start, stop)
from itertools import islice
from itertools import count
for i in islice(count(), 3, 15):
    print(i)
    

# starmap(function, iterable)
from itertools import starmap
def add(a, b):
    return a+b

for item in starmap(add, [(2,3), (4,5)]):
    print(item)


# takewhile(predicate, iterable)
from itertools import takewhile
print (list(takewhile(lambda x: x<5, [1,4,6,4,1])))


# tee(iterable, n=2)
from itertools import tee
data = 'ABCDE'
iter1, iter2 = tee(data)
for item in iter1:
    print(item)

#A
#B
#C
#D
#E

for item in iter2:
    print(item)

#A
#B
#C
#D
#E


# zip_longest(*iterables, fillvalue=None)
from itertools import zip_longest
for item in zip_longest('ABCD', 'xy', fillvalue='BLANK'):
    print (item)

#('A', 'x')
#('B', 'y')
#('C', 'BLANK')
#('D', 'BLANK')