

# --------------- Q1 -----------------
def sqrt(x):
    """
    Finding square root of a perfect number

    input -- an integer value, should be greater than zero
    Return -- square root of x
    
    """
    # ans var is binded here only locally
    ans = 0
    num_guess = 0
    if x > 0:
        while ans*ans <x:
            ans = ans+1
            num_guess+=1
            # print(ans,x)
        if ans*ans !=x:
            print(ans)
            return None
        else:
            print("square root of",x,"=",ans," and number of guesses =",num_guess)
            return ans,num_guess
    else:
        print(x,"is less than zero")

test = sqrt(1024)
print(test)
test = sqrt(43)
print(test)


# ---------------------Q2-------------------

def count(num_heads, num_legs):
    """
    inputs:
        num_heads : total number of heads, pos int
        num_legs: total number of legs, positive int
    
    """
    num_pigs = 0
    for num_chicks in range(0,num_heads+1):
        num_cows = num_heads - num_chicks
        total_legs = 2 * num_chicks + 4*num_cows
        if total_legs == num_legs:
            return (num_chicks, num_cows)
    return None,None


def how_many_in_yard():
    heads = int(input("how many heads? "))
    legs = int(input("how many legs? "))

    chicks, cows = count(heads, legs)
    if chicks == None:
        print("not equal distribution")
        return None
    else:
        print("there is",chicks,"chickens in the yard")
        print("there is",cows,"cows in the yard")

count = how_many_in_yard()
