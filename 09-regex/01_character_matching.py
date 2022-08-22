import re

text = 'abcdfghijk'
parser = re.search('a[b-f]*f', text)

print (parser.group())
# abcdf

# 20 most common regular expression
# https://regexland.com/most-common-regular-expressions/

#####################
# 1. Matching Numbers 

# To match whole numbers with one or more digits, 
# use the digit character \d+ like this:
text = 'abc123456'
parser = re.search('abc\d+', text)

print (parser.group())

# To include negative whole numbers
text = '-122345'
parser = re.search('-?\d+', text)

print (parser.group())

# For matching decimal numbers with a period . as decimal separator
# Replace the \. above with a , to match a decimal number with 
# a comma separator , instead.
text = '-1234.25'
parser = re.search('-?\d+(\.\d*)', text)

print (parser.group())


#####################
# 2. Replacing A Matched Term
# Syntax
# re.sub(pattern, repl, string, count=0, flags=0)
input = "The colour of my shirt matches the colour of my tie."
print(re.sub('colour', 'color', input))

# Replace multiple substrings with the same string
str = 'aaa@gmail.com bbb@hotmail.com ccc@apple.com'
print(re.sub('[a-z]*@', 'info@', str))

# Replace multiple different strings with the same string
str = 'aaa@gmail.com bbb@hotmail.com ccc@apple.com'
print(re.sub('gmail|hotmail|apple', 'appdividend', str))


#####################
# 3. Matching Text
# (both upper and lowercase) [A-Za-z], numbers [0-9], 
# spaces \s, and basic punctuation such as periods commas, 
# dashes, parentheses, etc.
text = 'spaces, and basic punctuation such as saidul'
parser = re.search('[A-Za-z0-9\.,;:!?()]+', text)

print (parser.group())


#####################
# 4. Matching Email Addresses
text = 'test@gmail.com'
parser = re.search('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', text)

print (parser.group())


#####################
# 5. Matching Special Characters
# Ex. matching the tilde sign ~
text = 'tilde\x7E'
parser = re.search('[\x7E]', text)

print (parser.group())

#####################
# 6. Matching Words
text = 'color of my shirt matches'
parser = re.search('\w+', text)

print (parser.group())


#####################
# 7. Matching URL
text = 'https://www.google.com'
parser = re.search('(?:http|https|ftp|mailto|file|data|irc):\/\/[A-Za-z0-9\-]{0,63}(\.[A-Za-z0-9\-]{0,63})+(:\d{1,4})?\/*(\/*[A-Za-z0-9\-._]+\/*)*(\?.*)?(#.*)?', text)

print (parser.group())

#####################
# 8. Matching date
# For dates in the format mm/dd/yyyy
text = '03/15/2022'
parser = re.search('^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$', text)
# For dates in the format yyyy/mm/dd
# ^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$
# For date in the format dd/mm/yyyy
# ^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$
print (parser.group())

#####################
# 8. Matching HTML tags
# To match an open or a close tag
# More examples can be found here https://www.pythonsheets.com/notes/python-rexp.html
text = '<img src="test.jpg" width="100%"/>'
parser = re.search('<[^>]+>', text)

print (parser.group())

#####################
# 8. Matching phone number
text = 'Here is my number 313-205-6589'
parser = re.search('(?:\(?\d{3})?\)?[- ]?[2-9]\d{2}[- ]?\d{4}', text)

print (parser.group())
