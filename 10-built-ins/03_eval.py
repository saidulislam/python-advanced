 # The eval built-in is fairly controversial in the Python community. The reason for 
 # this is that eval accepts strings and basically runs them. If you want to allow users 
 # to input any string to be parsed and evaluated by eval, then you just created a major 
 # security breach. However, if the code that uses eval cannot be interacted with by the 
 # user and only by the developer, then it is okay to use. Some will argue that it’s still 
 # not safe, but if you have a rogue developer, they can do a lot more harm doing other 
 # things than using eval.

some_val = 10
source = "some_val * 2"

print(eval(source)) # this is some crazy stuff. I still wouldn't recommend this

