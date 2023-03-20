class Bank:
    def __init__(self, dollars, ruppis, afghani):
        self.dollars = dollars
        self.ruppis = ruppis
        self.afghani = afghani

    def __str__(self):
        return f"USD$ {self.dollars} INR {self.ruppis} Afg {self.afghani}"

    # OVERLOADING OPERATOR: we can add, self refers to the objects on the left and other refers to the object on the right side of +
    def __add__(self,other):
        usd = self.dollars + other.dollars
        inr = self.ruppis + other.ruppis
        afg = self.afghani + other.afghani
        return Bank(usd, inr, afg)


king = Bank(100,32,21)
palwa = Bank(2,21,2)

# usd = king.dollars + palwa.dollars
# inr = king.ruppis + palwa.ruppis
# afg = king.afghani + plawa.afghani

# total = Bank(usd, inr, afg)

# OVERLOADING

print(king + palwa)
