class Set:
    def __init__(self,vals):
        self.vals = vals
    
    def insert(self,e):
        if e not in self.vals:
            self.vals.append(e)
    
    def remove(self,e):
        try:
            self.vals.remove(e)
        except ValueError:
            print(f"{e} is not found")
    
    def member(self, e):
        return e in self.vals
    
    def __str__(self):
        return f"{self.vals}"
    
    def display(self):
        vals = " "
        for e in sorted(self.vals):
            vals = vals + str(e) + ","
        return (f"({vals[:-1]})")


    def intersect(self, other):
        """Assumes other is an intSet
           Returns a new intSet containing elements that appear in both sets."""
        # Initialize a new intSet    
        commonValueSet = Set()
        # Go through the values in this set
        for val in self.vals:
            # Check if each value is a member of the other set    
            if other.member(val):
                commonValueSet.insert(val)
        return commonValueSet


set = Set("")
set.insert(4)
set.insert(40)
set.insert(4)
print(set)
print(set.member(3))
print(set.display())




def intersect(setB,setA):
    inters = []
    for e in setA:
        if e in setB:
            inters.append(e)
    return inters

a = [3,3,2,1,21,21,2,0]
b = [3,4,3,12,21,3,12,0]
i = intersect(a,b)
print(i)