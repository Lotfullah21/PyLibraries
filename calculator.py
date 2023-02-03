x = float(input("enter the first number "))
y = float(input("enter the second number "))
summation = x + y 
divison = round(x/y, 4)
print(f"{summation:,}")
print(f"{divison:,}")


z = "123232"
w = int(0)
for ch in z:
    w = w + int(ch)

def main():
    min = int(input("enter the minutes "))
    kms = int(input("enter the distance "))
    time = min_to_sec(min)
    miles = mile_to_km(kms)
    speed_per_sec = miles/time
    sec_to_min = time/60
    speed_per_min = miles/sec_to_min
    print("the average speed per second is", speed_per_sec)
    print("the average speed per minutes is", speed_per_min)


def min_to_sec(mins):
    seconds = mins * 60  + 42
    print("there are",seconds,"seconds in", mins,"minutes")
    return seconds

def mile_to_km(kms):
    miles = kms/1.16
    print("there are ",miles,"miles in",kms,"kilometers")
    return miles

main()


# print(w) 


# print(type(z))