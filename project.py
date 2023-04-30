def main():
    n = int(input("Number: "))
    print(fibonacci(n))
    print(factorial(n))
    print(sum_series(n))


def fibonacci(n):
    if n ==0:
        return 0
    elif n<0:
        return "incorrect input"
    elif n==1:
        return 1 
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def sum_series(n):
    sum_1 = 0
    for i in range(1,n+1):
        sum_1 = sum_1 + (1/i)
    return round(sum_1,3)

if __name__ =="__main__":
    main()