

# def mult(a,b):
#     result = 0
#     while b > 0:
#         result = result + a
#         b = b -1
#         print(f"result = {result},b = {b}")
#     return result


# d = mult(21,3)
# print(d)



# --------------- Recursion Algorithm -----------------

# here we need to divide the problem until we reach to a base case.

# def mult(a,b):
#     if b==1:
#         return a
#     else:
#         return a  + mult(a,b-1)


# d = mult(21,3)
# print(d)


# Factorial


def factorial(n):
    prod = 1
    for i in range(1,n+1):
        prod = prod*i
    return prod


print(factorial(5))

# ---- Recursive

# def factorial(n):
#     if n ==1:
#         return 1
#     else:
#         result = n*factorial(n-1)
#         return result

# print(factorial(5))
# print(a)


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    # '''
    # base = base
    power = 1
    while exp > 0:
        power = power * base
        # the value of pow which we observe in print fn, it is after going once through the loop, pow* base = 1 * 2 = 2
        # in each iteration we just multiply the power by 2,the iteration number is based the condition we specified, base is fixed
        print("iteration =",exp,"base=",base ,"power=",power,sep= " ")
        exp = exp -1

    return power

d = iterPower(2, 3)
print(d)


# ------------------ Recursive ---------- 

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here

    if exp == 0:
        return 1
    else:
        return base*recurPower(base, exp-1)
    
f = recurPower(3, 2)
print(f)