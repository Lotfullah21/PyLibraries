

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


# def factorial(n):
#     prod = 1
#     for i in range(1,n+1):
#         prod = prod*i
#     return prod


# print(factorial(5))

# ---- Recursive

# def factorial(n):
#     if n ==1:
#         return 1
#     else:
#         result = n*factorial(n-1)
#         return result

# print(factorial(5))
# print(a)


# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
 
#     returns: int or float, base^exp
#     # '''
#     # base = base
#     power = 1
#     while exp > 0:
#         power = power * base
#         # the value of pow which we observe in print fn, it is after going once through the loop, pow* base = 1 * 2 = 2
#         # in each iteration we just multiply the power by 2,the iteration number is based the condition we specified, base is fixed
#         print("iteration =",exp,"base=",base ,"power=",power,sep= " ")
#         exp = exp -1

#     return power

# d = iterPower(2, 3)
# print(d)


# # ------------------ Recursive ---------- 

# def recurPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
 
#     returns: int or float, base^exp

    # Your code here

#     if exp == 0:
#         return 1
#     else:
#         return base*recurPower(base, exp-1)
    
# f = recurPower(3, 2)
# print(f)


def fib(n):
    global num_calls
    num_calls = num_calls + 1
    if n==0 or n==1:
        return 1
    else:
        # print(num_calls)
        return fib(n-1) + fib(n-2)
        
# print(fib(10))  
def test_fib(n):
    for i in range(n+1):
        global num_calls
        num_calls = 0
        print("fibbonaci of ",i, "is",fib(i), "and number of calls = ", num_calls)
        # return "okay"

print(test_fib(40))








# def is_Palindrom(s):
    
#     def toChar(s):
#         s = s.lower()
#         letters = ""
#         for c in s:
#             if c in "asdfghjklopiuytreewqzxcvbnm":
#                 letters = letters + c
#         return letters
#     def ispal(s):
#         if len(s)<=1:
#             return True
#         else:
#             print(s)
#             return s[0]==s[-1] and ispal(s[1:-1])
#     return ispal(toChar(s))

# print(is_Palindrom("abcdedf, ghhg_fedcba"))