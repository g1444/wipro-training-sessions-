import re
pattern=r"\d{10}"
pattern_email=r"[a-zA-z0-9+-.%]+@[a-zA-Z.-]+\.[a-zA-z]{2,}"
result=re.fullmatch(pattern,"9876542362")
result_email=re.fullmatch(pattern_email,"gowthamreddy609@gmail.com")
if result:
    print("matched")
if result_email:
    print("matched")