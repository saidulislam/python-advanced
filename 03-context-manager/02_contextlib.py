from contextlib import contextmanager

@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print('Closing file')
        f_obj.close()

if __name__ == '__main__':
    with file_open('test.txt') as fobj:
        fobj.write('Testing context managers')
        
# contextlib.closing
from contextlib import contextmanager

@contextmanager
def closing(db):
    try:
        yield db.conn()
    finally:
        db.close()
        
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.google.com')) as webpage:
    for line in webpage:
        # process the line
        pass


from contextlib import suppress

with suppress(FileNotFoundError):
    with open('fauxfile.txt') as fobj:
        for line in fobj:
            print(line)

# contextlib.redirect_stdout / redirect_stderr
import sys

path = 'text2.txt'

with open(path, 'w') as fobj:
    sys.stdout = fobj
    help(sum)
    
# you can also do the following
from contextlib import redirect_stdout

path = 'text3.txt'
with open(path, 'w') as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)