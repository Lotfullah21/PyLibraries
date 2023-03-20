class Fraction:
    def __init__(self,num,den):
        self.num = num
        self.den = den

    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den
    
    def __add__(self, other):  
        numerator = self.num * self.den + self.den * self.num
        denominator = self.num * self.den
        return numerator / denominator
    
    def __str__(self):
        return (f"{self.num}/{self.den}")
    
    def __len__(self):
        return 1

half = Fraction(2,2)
zero = Fraction(1,1)
print(half)
print(half.getNum())
print(half.getDen())
print(half + zero)
print(half.__len__())