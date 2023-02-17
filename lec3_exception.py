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


            

def main():
    summation = get_sum()
    print(summation)

def get_sum():
    while True:
        try:
            x = int(input("Enter X ? "))
            y = int(input("Enter Y ? "))
        except:
            pass
        else:
            break
    return x+y

main()