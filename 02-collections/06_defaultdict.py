# Counting words in a sentence
sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

reg_dict = {}
for word in words:
    if word in reg_dict:
        reg_dict[word] += 1
    else:
        reg_dict[word] = 1

print(reg_dict)
# {'The': 1, 'red': 1, 'for': 2, 'jumped': 1, 'over': 1, 'the': 2, 'fence': 1, 'and': 1, 'ran': 1, 'to': 1, 'zoo': 1, 'food': 1}

# You can do the same with the defaultdict
from collections import defaultdict

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)


# Trying Python list type as default_factory
my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

reg_dict = {}
for acct_num, value in my_list:
    if acct_num in reg_dict:
        reg_dict[acct_num].append(value)
    else:
        reg_dict[acct_num] = [value]

print(reg_dict)

# Now let’s re-implement this code using defaultdict
from collections import defaultdict


my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

d = defaultdict(list)
for acct_num, value in my_list:
    d[acct_num].append(value)

print(d)
# defaultdict(<class 'list'>, {1234: [100.23, 75.0, 35.67], 345: [10.45, 222.66], 678: [300.25]})

# Using lambda as defaultfactory
from collections import defaultdict
animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'

print (animal['Nick'])
print (animal)
# Monkey
# defaultdict(<function <lambda> at 0x7fec755c6ea0>, {'Sam': 'Tiger', 'Nick': 'Monkey'})

