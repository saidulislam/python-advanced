from collections import Counter

print (Counter('superfluous'))
# Counter({'u': 3, 's': 2, 'p': 1, 'e': 1, 'r': 1, 'f': 1, 'l': 1, 'o': 1})

mylist = ["saidul", "hamza", "saidul", "Saidul"]
print(Counter(mylist))
# Counter({'saidul': 2, 'hamza': 1, 'Saidul': 1})

counter = Counter('superfluous')
print (counter['u'])
# 3

# think of this as a “scrambler”
counter = Counter('superfluous')
print (list(counter.elements()))
# ['s', 's', 'u', 'u', 'u', 'p', 'e', 'r', 'f', 'l', 'o']

# most common
counter = Counter('superfluous')
print( counter.most_common(2))
# [('u', 3), ('s', 2)]

# subtract() method
counter_one = Counter('superfluous')
print (counter_one)
#Counter({'u': 3, 's': 2, 'p': 1, 'e': 1, 'r': 1, 'f': 1, 'l': 1, 'o': 1})

#basically takes out each of the characters from 'super'
counter_two = Counter('super')
print(counter_one.subtract(counter_two))
#None

print (counter_one)
#Counter({'u': 2, 's': 1, 'f': 1, 'l': 1, 'o': 1, 'p': 0, 'e': 0, 'r': 0})
