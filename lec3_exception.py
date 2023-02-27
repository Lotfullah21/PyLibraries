# We use exception when something does not go will and we want our program to run smoothly irrespective of our error

# Synytax errors means something is wrong with the structure of our code, which python cannot parse or read them, easy to catch
# print("Hello)


# x = input("what is x ? ")
# y = input("what is y ? ")

# print(x+y)


# x = int(input("what is x ? "))
# y = int(input("what is y ? "))


# print(x+y)

# try:
#     x = int(input("what is x ? "))
#     y = int(input("what is y ? "))
# except:
#     print("x and y, both of them should be integers")
# else:
#     print(x+y)
    

"""
Lets define an infinite loop so that until the user gives us a correct input
we will be continuing our execution.

becuse True is always True

Remember until the user do not pass a valid value, no value would be save from left to right to the x variable.

Note: Try and exceptions are statements not functions.
"""

# while True:
#     try:
#         x = int(input("what is x ? "))
#         y = int(input("what is y ? "))
#     except ValueError:
#         print("x and y, both of them should be integers")
#     else:
#         break
# print(x+y)



# def main():
#     summation = get_sum()
#     print(summation)

# def get_sum():
#     while True:
#         try:
#             x = int(input("Enter X ? "))
#             y = int(input("Enter Y ? "))
#         except:
#             print("X and Y both of them should be integers")
#         else:
#             break
#     return x+y

# main()




# while True:
#     try:
#         x = int(input("Enter a valeu: "))
#         print(x)
#         print("Okay")
#     except ValueError:
#         print("Not Okay")
#     else:
#         break

# print("Correct way of a number")



# def  get_ratios(L1,L2):
#     """
#     Assume L1 and L2 are the same lenght
#     return L[1]/L[2]
#     """

#     ratios = []
#     for i in range(len(L2)):
#         try:
#             ratios.append(L1[i]/L2[i])
#         except ZeroDivisionError:
#             ratios.append("Nan")
#     return ratios

# L1 = [2,3,1,12]
# L2 = [2,12,0,1]
# ratio_list = get_ratios(L1,L2)
# print(ratio_list)



# def get_grades(data):
    
#     grades = []
#     for ele in data:
#         grades.append([ele[0],ele[1], avg(ele[1])])
#     return grades

# def avg(marks):
#     try:
#         return sum(marks)/len(marks)
#     except ZeroDivisionError:
#         return 0


# L1 = [[["king","sekandar"],[2,3,1,12]],[["mark","sam"],[0,0]],[["ali","aaysh"],[]]]
# # print(L1[0])
# print(get_grades(L1))





# def main():
#     summation = get_sum()
#     print(summation)

# def get_sum():
#     while True:
#         try:
#             x = int(input("Enter X ? "))
#             y = int(input("Enter Y ? "))
#         except:
#             pass
#         # break statement will be executed only when try statement  gets executed
#         else:
#             break
#     return x+y

# main()




















# def fancy_divide(numbers,index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError:
#         print("-1")
#     else:
#         print("1")
#     finally:
#         print("0")



# def fancy_divide(numbers, index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError:
#         fancy_divide(numbers, len(numbers) - 1)
#     except ZeroDivisionError:
#         print("-2")
#     else:
#         print("1")
#     finally:
#         print("0")




# def fancy_divide(numbers, index):
#     try:
#         try:
#             denom = numbers[index]
#             for i in range(len(numbers)):
#                 numbers[i] /= denom
#         except IndexError:
#             fancy_divide(numbers, len(numbers) - 1)
#         else:
#             print("1")
#         finally:
#             print("0")
#     except ZeroDivisionError:
#         print("-2")



# def fancy_divide(list_of_numbers, index):
#     try:
#         try:
#             raise Exception("0")
#         finally:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#     except Exception as ex:
#         print(ex)

# print(fancy_divide([0, 2, 4], 0))
# print(fancy_divide([0, 2, 4], 4))
# print(fancy_divide([0, 2, 4], 1))



def normalize(numbers):
    max_numbers = max(numbers)
    norm = []
    for i in range(len(numbers)):
        number = numbers[i]/max_numbers
        norm.append(number)
    return norm

a = normalize([1,3,1,12])
print(a)
