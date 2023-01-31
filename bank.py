class Account:
    def __init__(self):
        self._balance = 0
    
# a property is an instance variable, that is protected in how to read or how to write in it.

    @property
    def balance(self):
        return self._balance
    
    def deposit(self,n):
        self._balance += n

    def withdraw(self,n):
        self._balance -= n
    
def main():
    account = Account()
    print("Balance",account.balance)
    account.deposit(100)
    account.withdraw(29)
    print("Balance",account.balance)

if __name__ == "__main__":
    main()






# balance = 0




# def main():
#     print("Balance:",balance)
#     withdraw(108)
#     deposit(90)
#     print("Balance:",balance)

# def deposit(n):
#     global balance
#     balance -= n

# def withdraw(n):
#     global balance
#     balance +=n

# if __name__ == "__main__":
#     main()