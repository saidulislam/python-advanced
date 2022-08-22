my_list = [1, 2, 3]

print (iter(my_list))

list_iterator = iter(my_list)
print (next(list_iterator))
print (next(list_iterator))
print (next(list_iterator))
#print (next(list_iterator)) # this will throw exception

my_list = [1, 2, 3]
for item in iter(my_list):
    print(item)


