import re
empid="EMP123"
result=re.match(r"^EMP\d{3}",empid)
if result:
    print("True")