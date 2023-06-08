
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


def is_prime(num):
    prime = True
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            prime = False
            # break out of loop
            break

    # check if flag is True
    if prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


p = is_prime(17)
print(p)

x = y = 10
print(x,y)
