# pronounced “deck”

# As a general rule, if you need fast appends or fast pops, use a deque. 
# If you need fast random access, use a list.

# deque is thread safe and fast fast
from collections import deque
import string
d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)
    
# Testing different deque methods
from collections import deque
import string
d = deque(string.ascii_lowercase)
for letter in d:
    letter
d.append('bork')
print(d)


d.appendleft('test')
print(d)

# bring the last item to the front
d.rotate(1)
print(d)


# handle files with deque
from collections import deque

def get_last(filename, n=5):
    """
    Returns the last n lines from the file
    """
    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        print("Error opening file: {}".format(filename))
        raise

print(get_last("/Users/saidulislam/Python-Projects/python-advanced/test.txt"))