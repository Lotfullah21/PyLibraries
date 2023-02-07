
def mult(a = False, b=False):
    if a and b:
        print(a*b)
    elif a:
        print(a)
    else:
        print(b+2)


mult(12,21)


# we can use * to have as many arguments as we want

def sumation(*nums):
    total = 0
    for n in nums:
        total = total + n
        avg = total/len(nums)
    print("total",total,"averate",avg)
    return total, avg
    
d = sumation(2,211,12,12)