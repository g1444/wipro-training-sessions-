import re
t="gowtham is good boy"
m=re.search("gowtham",t)
print(m.span())
if m:
    start,end=m.start(),m.end()
    print(f"found in {start},{end}")
else:
    print(m)
# 
tooo="gooo gooo"
result=re.search("gooo",tooo)
print(result.group())
# result=re.findall("go",t)
# print(result.start(),result.end())
k=t.replace(" ","")
print(k)