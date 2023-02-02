# Strings 

alphabets = "aabcdefghjiklmnufxzc"

# Using range function 

# for cr in range(len(alphabets)):
#     if alphabets[cr] == "a":
#         print("found ", alphabets[cr])

# -- Using for loop only

# for alpha in alphabets:
#     if alpha == "a" or alpha == "s":
#         print("got the alpha", alpha)
#     else:
#         print(alpha,"is not an alpha")


# words = "ABCDQWERTYUUIPLKJHGFDSAZXCVBNMzxcvbnmlkjhgfdsaawqertyuioppoiuytrweqed"
# word = "Brain"
# # word = input("Enter a word! ")
# times = 5;    
# # times = int(input("how enthusiastic you are"))
# i = 0
# while i<len(word):
#     w = words[i]
#     if w in words:
#         print("Give me a",w, w,"!")
#     i = i + 1

# print("How does this spell")
# for wo in word:
#     print(word)



# --- Using For loop

words = "ABCDQWERTYUUIPLKJHGFDSAZXCVBNMzxcvbnmlkjhgfdsaawqertyuioppoiuytrweqed"
word = "Brain"
# word = input("Enter a word! ")
times = 5;    
# times = int(input("how enthusiastic you are"))
i = 0
for w in words:
    if w in words:
        print("Give me a",w, w,"!")
    i = i + 1

print("How does this spell")
for wo in word:
    print(word)