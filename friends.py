
friends = []

with open("info.csv") as file: # normally, if r , w , or a is not mentioned, by default, it is reading , "r"
    for line in file:
        name,country = line.rstrip().split(",")
        friends.append(f"{name} is living in {country}")
for friend in sorted(friends):
    print(friend)


# with open("info.csv") as file: # normally, if r , w , or a is not mentioned, by default, it is reading , "r"
#     for line in file:

#         name,country = line.rstrip().split(",")
#         print(f" {name} is living in {country}")

#         # row = line.rstrip().split(",")
#         # print(f" {row[0]} is living in {row[1]}")