import re
mail="gowthamgmail.com"
if re.match(r"[a-zA-Z]+@",mail):
    print("valid")
else:print("invalid")