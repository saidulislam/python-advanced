# When you compile patterns, they will get automatically cached so 
# if you aren’t using a lot of regular expressions in your code, 
# then you may not need to save the compiled object to a variable
import re

text = "The ants go marching one by one"

strings = ['the', 'one']

for string in strings:
    regex = re.compile(string)
    match = re.search(regex, text)
    if match:
        print('Found "{}" in "{}"'.format(string, text))
        text_pos = match.span()
        print(text[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))