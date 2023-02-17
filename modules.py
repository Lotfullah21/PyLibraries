# """
# Libraries are files with one or more features written by others or by our self, we can use it when we need them, instead of
# cpying and pasting, 

# modules are libraries that have one or more functins and features that we can use

# import-> we can use this keyword to import the features from other module
# from -> it allows us to import specific features, methods or functions from a module
# """

# # import random
# import random
# from random import choice

# coin = random.choice(["head", "tail","Null"])
# print(coin)

# integer = random.randint(1,10)
# print(integer)

# cards = ["jack","queen", "king"]
# random.shuffle(cards)
# for i in cards:
#     print(i,"\n",end = " ")


# import statistics
# data = statistics.mean([100,100])
# print(data)

"""
Command_line arguments

by this we can give inputs while runing the program in command line

sys is a built in module that gives access to the values typed in command line, and by argv we can 
have access to all the values typed in there as a list
"""

import sys

# # in sys.argv[0], is name of the program
# try:
#     print("hello, my name is",sys.argv[1])
# except:
#     print("I think some thing missing")

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) >  2:
    print("Too many argumets, it should be two args")
else:
    print("HELLO",sys.argv[1])