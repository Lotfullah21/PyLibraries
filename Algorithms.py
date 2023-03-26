
def isPalindrom(str):
    startIndex = 0
    endEndex = len(str) -1 
    for x in str:
        if str[startIndex] == str[endEndex]:
            return True
    return False

print(isPalindrom("r"))



def reverse(str):
    """
    reverses a string
    input-> a string
    retturn-> reverse of a string
    """
    return str[::-1]

coffees = ["Alpachino","latte","Capacino"]

reversed_coffees = map(reverse, coffees)

for coffee in reversed_coffees:
    print(coffee)