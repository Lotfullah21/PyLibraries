class CreditCard:
    """A consumer credir card"""
    def __init__(self, customer, bank,accnt, limit):
        self.customer = customer
        self.bank = bank
        self.accnt = accnt
        self.limit = limit
        self.balance = 0
    
    def get_customer(self):
        return self.customer
    def get_bank(self):
        return self.bank
    def get_accnt(self):
        return self.accnt
    def get_limit(self):
        return self.limit
    def get_balance(self):
        return self.balance
    
    def charge(self, price):
        """ give the credit if price+balance<limit"""
        if price + self.balance > self.limit:
            return False
        else:
            self.balance = self.balance +  price

    def make_payment(self, amount):
        """"reduce from balance the amount given as argument"""
        if amount>self.balance:
            return "Not suufficient money"
        else:
            self.balance = self.balance - amount
    def __str__(self):
        return f"{self.customer} with account number {self.accnt} has $ {self.limit} of credit"



king = CreditCard("king","ICIC","3212 2132 2132",2000)
asif = CreditCard("Asif","ABI","2321 3232 3243",2090)
mulla = CreditCard("Rohid","SBI","2132 2133 1232",324)

if __name__ == "__main__":
    wallet = []
    wallet.append(king)
    wallet.append(mulla)
    wallet.append(asif)
    for val in range(10):
        wallet[0].charge(val)
        wallet[1].charge(3*val)
        wallet[2].charge(4*val)
    
    for c in range(3):
        print("Customer =",wallet[c].get_customer())
        print("Bank =",wallet[c].get_bank())
        print("Balance =",wallet[c].get_balance())
        print("Limit =",str(wallet[c].get_limit()))

        while wallet[c].get_balance()>100:
            wallet[c].make_payment(100)
            print("new balance",wallet[c].get_balance())


print("a"+"b")