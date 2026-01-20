import re
t="Gowtham is super hero"
result=re.match("Gowtham",t)
print(result)
if result:
    print("found")