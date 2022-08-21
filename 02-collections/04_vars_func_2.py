# Python program to illustrating
# the use of vars() and locals
# when no argument is passed and
# how vars() act as locals().
class DictionaryMaker(object):
    def __init__(self):
        self.num1 = 20
        self.num2 = "this is returned"
 
    def __repr__(self):
        return "DictionaryMaker() is returned"
 
    def loc(self):
        ans = 21
        return locals()
     
    # Works same as locals()
    def code(self):
        ans = 10
        return vars()
 
    def prog(self):
        ans = "this is not printed"
        return vars(self)
     
 
if __name__ == "__main__":
    obj = DictionaryMaker()
    print (obj.loc())
    print (obj.code())
    print (obj.prog())
    
# OUTPUT
# {'ans': 21, 'self': DictionaryMaker() is returned}
# {'ans': 10, 'self': DictionaryMaker() is returned}
# {'num1': 20, 'num2': 'this is returned'}