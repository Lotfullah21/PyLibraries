# # # tuples are generalized form of strings,it is also immutable

# # a = (2,)
# # print(type(a))

# # a_ = (2)
# # print(type(a_))

# # print(10*a)

# # print(10*a_)

# # # tuples can be contenated, indexed, sliced

# # a = (2,11,12,32)
# # b = (32,"hello", "hi")
# # print(a+b)
# # print(a[:3])

# # def find(a, b):
# #     result = ()
# #     for ele in a:
# #         if ele in b:
# #             result += (ele,)
# #     return result

# # same = find(a,b)
# # print(same)      



# # def extreme_divisior(n1, n2):
# #     """
# #     inputs: n1 and n2, both are integers,
    
# #     return: smallest and largest common divisor between n1 and n2 value which can be divided by both of the inputs, if not, 
# #     return None, None
    
    
# #     """
# #     max_val, min_val = None, None

# #     for i in range(2, min(n1,n2)+1):

# #         if n1%i ==0 and n2%i==0:

# #             if min_val == None:
# #                 min_val = i
# #             max_val = i
        
# #     return min_val, max_val


# # d = extreme_divisior(100, 200)
# # print(d)





# # def find_extreme_divisors(n1, n2):
# #  """Assumes that n1 and n2 are positive ints
# #  Returns a tuple containing the smallest common
# # divisor > 1 and 
# #  the largest common divisor of n1 & n2. If no
# # common divisor,
# #  other than 1, returns (None, None)"""

# #  min_val, max_val = None, None
# #  for i in range(2, min(n1, n2) + 1):
# #     if n1%i == 0 and n2%i == 0:
# #         if min_val == None:
# #             min_val = i
# #         max_val = i+
# #         print(min_val , max_val)
# #  return min_val, max_val


# # c = find_extreme_divisors(100, 200)
# # print(c)


# def get_info(aTuple):

#     nums = ()
#     words = ()
    
#     for t in aTuple:
#         nums = nums + (t[0],)
#         if t[1] not in words:
#             words = words + (t[1],)
#     mini = min(nums)
#     maxi = max(nums)
#     unique = len(words)
    
#     return (mini, maxi,unique)


# min , max, length = get_info(((12,"hello"),(3,"king"),(21,"king"),(32,"ali"),(332,"king secunder")))
# print(min, max, length)
    
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    
    tup = aTup[::2]
    return tup

odd = oddTuples(('I', 'am', 'a', 'test', 'tuple'))
print(odd)