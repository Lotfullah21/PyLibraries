
import re 

name = input("What is your name? ").title()

"""

.+ one or more of the things on the left
(.+) one or more of the things on the right side and capture them`
(.+) anything in () will be returned to us and using variable which we saved them we can access it using var.groups()
 * zero or more spaces, still it is going to capture it
 := warlus operator, assign the values from left to right and ask the boolean expression

"""


if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello {name}")


# if matches:
#     name = matches.group(2) + " " + matches.group(1)
# print(f"Hello {name}")

# if matches:
#     last = matches.group(1)
#     first = matches.group(2)
#     name = f"{first} {last}"
# print(f"Hello {name}")


# if matches:
#     first, last = matches.groups()
#     name = f"{last} {first}"

# print(f"Hello {name}")













# name = input("What is your name ? ").title()

# if "," in name:
#     first, last = name.split(", ")
#     print(f"Hello {last} {first}")