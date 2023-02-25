
import re

url = input("Enter your url ? ")


"""
any time we face special symbols in re like (.,$,&) we need to escape it using \.
? putting optional anything which is before ?, so s? means might be https or http
(:?) yes we gropu this , but do not capture this
"""

if matches  :=  re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9]+)",url,flags = re.IGNORECASE):
    print("UserName",matches.group(1))




# username =re.sub(r"^(https?://)?(www\.)?twitter\.com/"  ,  "",   url)
# print(username)



# url = input("Enter your url ? ")

# username = url.replace("https://twitter.com/","")
# print(username)