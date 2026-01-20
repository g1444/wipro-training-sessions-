import re
print("python","Python",re.I)

text2 ="one\ntwo\nthree"
print(re.findall(r"^t\w+",text2,re.M))