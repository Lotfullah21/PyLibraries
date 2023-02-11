
x = 16

ans = 0

while(ans**2)<16:
    ans = ans + 1
print(ans)


# or another way

x = 64
epsilon = 0.001
ans = 0
increment = 0.01

while abs(ans**2 - x) > epsilon:
    # print(ans)
    ans = ans + increment
print(ans)



x = 10

i = 1

while i < x:
    if x%i==0:
        print(i)
    i = i + 1
    # print(i)

x = 10
for var in range(1, x):
    # print(x%var ==0,var)


Tup = (21,1,3,4,5,7)
print(Tup[::2])


divisors = ()
x = 100

for var in range(1,x):
    if x%var ==0:
        # concatenation of tuples
        divisors = divisors + (var,)
print(divisors)



s1 = "21,21h, hello"
s2 = "king, hello"
print(s1,s2)
# indexing
print(s1[0],s1[-1])


s = "1234567890"
total = 0
for char in s:
    total = total + int(char)
    print(total)