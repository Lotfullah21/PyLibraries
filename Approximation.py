# Find cube root of a number 

cube = 271
epsiolon = 0.01
increment = 0.001
num_guess = 0
guess = 0
ctr = 0

while abs(guess**3 - cube) >= epsiolon and cube<=guess:

    guess = guess + increment
    num_guess = num_guess+1

    C:\Users\Lotfullah Andishmand\Desktop\Python\Code\Approximation.py
    ctr = ctr+1
print(num_guess)

if abs(guess**3 - cube) >= epsiolon:
    print("Cube root does not exist", cube)
else:
    print("the closes answer to", cube , "is", guess)