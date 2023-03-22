


def divide(a,b):
    return a/b

try:
    divide(2,0)
except Exception as e:
    print("something wrong happened",e)
    print(e.__class__)