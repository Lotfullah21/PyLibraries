def main():
    yell("this", "is", "king")

# * words means we have variable amount of inputs
def yell(*words):
    # map(functino,iterable,...), here we are calling the function on every iterable input and in retrurn we get a list of output
    uppercased = [word.upper() for word in words]
    map(str.upper,words)

    print(*uppercased) # unpacking the list

if __name__ == "__main__":
    main()











# def main():
#     yell(["this", "is", "king"])


# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(uppercased)
#     print(*uppercased) # unpacking the list

# if __name__ == "__main__":
#     main()


# def yell(words):
#     print(words.upper())

# if __name__ == "__main__":
#     main()