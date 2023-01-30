
# root = 16

# ans = 0 

# while ans * ans < root:

#     ans = ans + 1
#     print(ans, root)

# print(ans)

# if (root % 2 ) * 2 == 0:
#     print("even")
# else:
#     print("odd")


# root = -161

# ans = 0

# if root  > 0:
#     while ans * ans < root:

#         ans = ans + 1

#     if ans * ans != root:
#         print("No a perfect number")
    
#     else:
#         print (ans)
# else:
#     print("Not a Positive number")


# ---------- Finding the divisor --------------

# x = 42
# i = 1

# if x > 0:
#     while i < x:
#         if x % (i) ==0:
#             print(i)
#         i = i+1
# else:
#     print("Not a positive number")


x = 42
divisors = ()
if x>0:
    for var in range(1, x):
        if x%var ==0:
            # here adding means, concatenating two tuples
            divisors = divisors + (var,)
    print(divisors)
else:
    print(x, "is not a positive number")



digit = 2131

summation = str(0)

for c in str(digit):
    summation = summation + c
print(summation)



digit = 2131

summation = 0

for c in str(digit):
    summation = summation + int(c)
print(summation)