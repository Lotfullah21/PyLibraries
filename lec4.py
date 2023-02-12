

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


---------------------- Q3 -----------------

def count(num_heads, num_legs):
    """
    inputs:
        num_heads : total number of heads, pos int
        num_legs: total number of legs, positive int
    
    """
    for num_chicks in range(0,num_heads+1):
        for num_birds in range(0, num_heads - num_chicks + 1):
            num_cows = num_heads - num_chicks - num_birds
            total_legs = 2 * num_chicks + 2*num_birds  + 4*num_cows
            if total_legs == num_legs:
                return (num_chicks, num_birds, num_cows)
    return None,None,None


def how_many_in_yard():
    heads = int(input("how many heads? "))
    legs = int(input("how many legs? "))

    chicks,birds, cows = count(heads, legs)
    if chicks == None:
        print("not equal distribution")
        return None
    else:
        print("there is",chicks,"chickens in the yard")
        print("there is",cows,"cows in the yard")
        print("there is",birds,"birds in the yard")

count = how_many_in_yard()

----------- Q3, different method

def count(num_heads, num_legs):
    """
    inputs:
        num_heads : total number of heads, pos int
        num_legs: total number of legs, positive int
    
    """
    is_sloution_found = False
    for num_chicks in range(0,num_heads+1):
        for num_birds in range(0, num_heads - num_chicks + 1):
            num_cows = num_heads - num_chicks - num_birds
            total_legs = 2 * num_chicks + 2*num_birds  + 4*num_cows
            if total_legs == num_legs:
                # print("there is",num_chicks,"chickens in the yard")
                # print("there is",num_birds,"cows in the yard")
                # print("there is",num_cows,"birds in the yard")
                return (num_chicks, num_birds, num_cows)
                is_sloution_found = True

    if not is_sloution_found:
        print("No Solution!")
        return None,None,None

def how_many_in_yard():
    heads = int(input("how many heads? "))
    legs = int(input("how many legs? "))

    chicks,birds, cows = count(heads, legs)
    if chicks == None:
        print("not equal distribution")
        return None
    else:
        print("there is",chicks,"chickens in the yard")
        print("there is",cows,"cows in the yard")
        print("there is",birds,"birds in the yard")

count = how_many_in_yard()


------------ Q5 ----------------
Recursion


def isPalindrom(s):
    """
    inputs:
    here we are having two base cases, if the lenght of string is zero or 1, it is a palindrom, this can be our base case,
    untill the above condition is satisified we reduce the length of string and will check first and last element of the string

        a string
        output: to check if it is a palindrom or not
    
    """
    if len(s)<=1:
        print("Yes, it is a palindrom",s)
        return True
    else:
        print("Checking,it is a palindrom",s)
        return s[0]==s[-1] and isPalindrom(s[1:-1])


pal = isPalindrom("abccba")
print(pal)



def ispalindrom(s, indent):
    """
    a string
    output: to check if it is a palindrom or not    
    """
    print(indent)
    if len(s)<=1:
        print(indent)
        return True
    else:
        ans = s[0]==s[-1] and ispalindrom(s[1:-1], indent + indent)
        print(indent,"about to return", ans,s)
        return ans

pal = ispalindrom("abccba",indent=" ")
print(pal)



def fibbonacci(x):
    if x ==0 or x==1:
        return 1
    else:
        # print(x)
        ans =  fibbonacci(x-1)+fibbonacci(x-2)
        # print(fibbonacci(x-1),fibbonacci(x-2),ans)
        return ans
    
fib = fibbonacci(10)
print(fib)