
friends = ["King","Ayaan","Ustad","U_Hakim","Asif"]

def find_friend(friend):
    if friend[0] == "U":
        return False
    else:
        return friend

# using map, we will get the boolean values based on the values passes as return
new_friend = map(find_friend,friends)
for f in new_friend:
    print("Mapped",f)


# filter create a new list and append the values of the list which their boolean values had been True 
filter_friend = filter(find_friend, friends)
for f in filter_friend:
    print("Filtered",f)



some = ["aaa", "bbb"]

#1
# def aa(some):
#    return

# #2
# def aa(some, 5):
#    return

#3
# def aa():
#    return

# #4
def aa():
   return "aaa"

print(aa())