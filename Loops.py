# # print("me0w\n"*10, end = "")

# # for i in range(100):
# #     print("meow")

# # i = 0

# # while i <100:
# #     print("meow")
# #     i = i +1


# # i = 4

# # while i !=0:
# #     i = i - 1
# #     print(i,"meow")

# # for i in [0,12,2]:
# #     print("meow",i)


# # if not using variable, use _

# # for _ in range(10):

#     # print(10) 


# def main():

#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("enter a number "))
#         if n>0:
#             break
#     return n

# def meow(n):
#     for _ in range(n):
#         print("king")

# main()



def square(size):
    # for the amount of size, print that much rouw
    for i in range(size):
        # for the amount of row, print column, or go throw each row and print that much of column
        for j in range(size):
            # no new line after each time we go throug a new columns
            print("#",end = "")
        # print new line after going through each row
        print()
        # pass

square(3)