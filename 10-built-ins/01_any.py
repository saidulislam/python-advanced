# The any built-in accepts an iterable and will return True if any element in the given iterable is True.

print (any([0,0,0,1])) # at least one item in the list is True, 1


widget_one = ''
widget_two = ''
widget_three = 'button'
widgets_exist = any([widget_one, widget_two, widget_three])
print (widgets_exist)


# Python’s all built-in as it has similar functionality except 
# that it will only return True if every single item in the iterable is True.

print(all([1,1,1,1,1])) # True. Because all values are True
print(all([0,0,0,1])) # False. Because at least one item is false
