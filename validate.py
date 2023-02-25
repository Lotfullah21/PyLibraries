import re

email = input("what is your email address? ").strip()
"""

  .+ one or more of anything on the left
  []+ means one or more of anything on the left but only the ones inside[]
  [^]+ means one more of anything on the left except the one inside [].
  \w means alphabets uper lower, numbers 0-9 and underscore
  \s means space or (\w\s)

it is not necessary to invent the wheel which already had been invented
"""
if re.search(r"^[a-z0-9_\.]+@(\w+\.)?\w+\.(com|edu|in|gov)$", email,flags = re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")



# if re.search("^[a-zA-Z0-9]+@[A-Za-z0-9]+\.com$", email):
#     print("Valid")
# else:
#     print("Invalid")


# if re.search("^[^@]+@[^@]+\.com$", email):
#     print("Valid")
# else:
#     print("Invalid")



# if re.search("^[^@]+@[^@]+\.com$", email):
#     print("Valid")
# else:
#     print("Invalid")





# if re.search("^.+@.+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")














# username, domain = email.split("@")

# if username and email.endswith(".com"):
#     print("Valid")
# else:
#     print("Invalid")






# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")