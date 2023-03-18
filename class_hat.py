
    
import random

class Hat:
    # class variable can be shared among all the methods
    houses = ["Baghlan","Khost","Afghanistan","Paktia"]
    
    # class method is a function which does not have access to the self
    @classmethod
    def sort(cls,name):
        print(name,"is from",random.choice(cls.houses))

Hat.sort("King")