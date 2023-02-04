



--------------------- Approximation Algorithm -------------------------
in this kind of algorithm, we are not looking for exact solution, but rather to a close enough solution
initialize the guess, and an increment variable to a small value
initiliaze the epsilon variable to a boundry value, if it is small, we might an accurate answer, if it sets to a large
value, we might get a bigger value
we have to set when the while loop should stop, it cannot run forever

guess = 0
increment = 0.02
epsilon = 0.001
num_guess = 0
cube = 8000

while abs(guess**3 - cube) >= epsilon and num_guess< cube:
    guess +=increment
    num_guess+=1
    print(guess, num_guess)

if abs(guess**3-cube) < epsilon:
    print("approxmate cubic root of", cube, "is", guess,"with", num_guess, "guesses")
    print(guess, num_guess)

else:
    print("there is no approximate solution at this range for", cube)


------------ Infinite Loop ------------------

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step
        print(guess, step,abs(guess**2 -x))

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))


-------------------Bisection algorithm -------------------
throwing half possible numbers

x = 26
epsilon = 0.01
low = 1
high = x
guess = (high + low)/2
num_guess = 0

while abs(guess**2-x)>=epsilon and num_guess<=x:
    num_guess +=1
    guess = round(guess, 3)
    guess2 = round(guess**2, 2)
    print(x,guess ,guess2, num_guess,abs(guess**2-x))
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2
print(x,guess ,guess2, num_guess,abs(guess**2-x))
print('succeeded: ' + str(guess))




x = 0.25
epsilon = 0.01
low = 0
high = x
guess = (high + low)/2
num_guess = 0

while abs(guess**2-x)>=epsilon and num_guess<10:
    num_guess +=1
    guess = round(guess, 4)
    guess2 = round(guess**2, 4)
    print("x=",x,"guess=",guess ,"guess^2=",guess2,"iteration=",num_guess,"abs=", abs(guess**2-x))
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2
print("x=",x,"guess=",guess ,"guess^2=",guess2,"iteration=",num_guess,"abs=", abs(guess**2-x))
print('succeeded: ' + str(guess))


------------NEWTON-RAPHSON METHOD ---------

given a guess g, a better guess is = g - f(g)/f'(g)

epsilon = 0.001
c = 162
guess = c/1
num_guess = 0
while abs(guess**2-c)>=epsilon:
    guess = guess - (guess**2 -c)/(2*guess)
    num_guess = num_guess+1
print(guess, num_guess)


