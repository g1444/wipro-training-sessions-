import re
result=re.finditer(r"\d+","this is 21,5,6,77,78, hello")
for n in result:
    print(n.group(),n.span())

m=re.search(r"\w+(?=@)","test@gmail.com")
print(m.group(),m.span())