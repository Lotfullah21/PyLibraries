
def main():

    n = int(input("height of pyramid ? "))
    pyramid(n)


def pyramid(n):
    for i in range(n):
        # print(i,end = "  ")    used for debugging purpose
        print("#" * (i+1))


if __name__ == "__main__":
    main()