import re
text = """
Hello, contact us at support@test.com.
You can also reach admin@company.co.in later.
"""
pattern=r"\d+\s\w+"
m=re.findall(pattern,text)
print(m)