# Python program to illustrate
# working of vars() method in Python

class DictionaryMaker:
    def __init__(self, name1 = "Arun", num2 = 46, name3 = "Rishab"):
        self.name1 = name1
        self.num2 = num2
        self.name3 = name3

dm = DictionaryMaker()
print(vars(dm))

# OUTPUT
# {'name1': 'Arun', 'num2': 46, 'name3': 'Rishab'}