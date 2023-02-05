# x = int(input("what is x ? "))

# y = int(input("what is y ? "))

# if x > y:
#     print(x, "is greater than", y)


# if x==y:
#     print("X == Y")
# else:
#     print(x, "is less than", y)


def main():
    
    n = int(input("enter a number ? "))

    if is_even(n):
        print(n,"is an even number")
    else:
        print(n,"is not an even number")

def is_even(n):
    
    return n%2==0
    # return True if n%2==0 else False
    # if n%2==0:
    #     return True
    # else:
    #     False



main()