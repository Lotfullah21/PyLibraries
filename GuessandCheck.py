
# cube = 8

# for guess in range(cube+1):
#     if guess **3 ==cube:
#         print(guess)

cube = -64

for guess in range(abs(cube)):
    
    if guess**3 >= abs(cube):
        break
    print(guess, guess**3)
if guess**3 != abs(cube):
    print("there is no perfect cube")
else:
    if cube < 0:
            guess = -guess
    print(guess,guess**3)
