
# friends = {"rich":"Ayaan","humble":"Rithik"}

# # print(friends)

# for friend in friends:
#     print(friend, friends[friend], sep=" , ")


friends = [
    {"name":"Ayaan","wealth":"$200021"},
    {"name": "Rithik","wealth":"$121" }
    ]

for friend in friends:
    print(friend["name"], friend["wealth"], sep=" , ")
