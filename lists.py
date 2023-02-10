

# # # # L1 = [2, 201,21]
# # # # L2 = L1[-1::-1]
# # # # print(L2)

# # # # L = [1, 2, 3]
# # # # L.append(L)
# # # # print(L is L[-1])

# # # # # --------------- List comprehension -------------------
# # # # # List comprehension provides a concise way to apply an operation
# # # # # to the sequence values provided by iterating over an iterable value

# # # # d = [e**2 for e in range(10) if e%2==0]
# # # # print(d)

# # # # d = [ele**2 for ele in [3,2,1,"21","hello"] if type(ele)==int]
# # # # print(d)


# # # # d = [[] for _ in range(4)]
# # # # print(d)

# # # # d = [(x,y) 
# # # #      for x in range(5) if x%2==0
# # # #      for y in range(5) if y%2==0
# # # #      ]
# # # # print(d)


# # # # d = [[(x,y) for x in range(5) if x%2==0]
# # # #      for y in range(5) if y%2==0
# # # #      ]
# # # # print(d)

# # # # def gen_primes():
# # # #     primes = []
# # # #     for x in range(2,10):
# # # #         is_prime = True
# # # #         for y in range(3,x):
# # # #             if x%y ==0:
# # # #                 is_prime = False
# # # #         if is_prime:
# # # #             primes.append(x)
# # # #     return primes
# # # # p = gen_primes()
# # # # print(p)

# # # # d = [x for x in range(2, 10) if all(x % y != 0 for y in
# # # # range(3, x))]
# # # # print(d)

# # # def is_prime(a):
# # #     prime = True
# # #     for i in range(2, a):
# # #         if a%i==0:
# # #             prime = False
# # #             break
# # #     if prime:
# # #         print(a, "is a prime")
# # #     else:
# # #         print(a, "not a prime")
# # #     return "okay"


# # # p = is_prime(1117)
# # # print(p)

# # # ------------------ Higher order programming ----------------------- 


# # # def apply(L,f):
# # #     for i in range(len(L)):
# # #         L1 = L[:]
# # #         L[i] = f(L[i])
# # #     return L1, L
# # #     # print(L[i])
# # #     # return L[i]

# # # L  = [3.2,1.2,12,12.3132,-32]

# # # a = apply(L, abs)

# # # print(a)

# # # a = apply(L, lambda x: x**2)
# # # print(a)

# # # a = apply(L , int)
# # # print(a)

# # # # Map function is also a hihger order operation, but more general form, 
# # # # the first argument is a function, the 2nd argument is the paramteres we want to apply the function to

# # # a = list(map(str, range(10)))

# # # print(a)


# # # a = [str(ele) for ele in range(10)]
# # # print(a)

# # # for i in map(lambda x: x**2, range(3)):
# # #     print(i)


# # # L1 = [2,21]
# # # L2 = [322,0]

# # # for i in map(max, L1,L2):
# # #     print("max", i,L1,L2)

# # def rise(L1,L2):
# #     """L1, L2 lists of same length of numbers
# #  returns the sum of raising each element in L1
# #  to the power of the element at the same index in L2
# #  For example, f([1,2], [2,3]) returns 9"""
# #     sum = 0
# #     # map(function, variable)
# #     for i in map(lambda L1,L2: L1**L2, L1,L2):
# #         sum = sum + i
# #         print(i,L1,L2,sum)
# #     return sum

# # print(rise([2,2,3],[1,1,3]))



# # print('My favorite professor-John G.-rocks'.split(' '))
# # print('My favorite professor-John G.-rocks'.split('-'))
# # print('My favorite professor-John G.-rocks'.split('_'))


# L = [0,12,21,12,12,1,2,3,4,5,6,87,43]
# L1 = sorted(L)
# print(L,L1,end ="\n\n")


# g = ["a","b","e","ed","aa"]
# e = ["a","e","r","4"]
# w = g.sort
# print(g)

# print(g > e)



# listA = [1, 4, 3, 0]
# print(listA.sort())
# print(listA.insert(0,100))
# print(listA.index(1))
# print(listA.extend([4, 1, 6, 3, 4]))

# listA.sort()
# listA.insert(0,100)
# listA.remove(3)
# listA.append(3)
# # print(listA)


# listB = ['x', 'z', 't', 'q']
# print(listB.sort())
# print(listB.pop())


def apply_func(f,L):
    for fn in f:
        for ele in L:
            f = fn(ele)
            print(f,end = " ")
    return f

d = apply_func([abs,int, float],[4,-32,12,42])
print(d)



def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

def maxi(a):
    return max(0,4)

d = applyEachTo([inc,maxi,int], -3)
print(d)