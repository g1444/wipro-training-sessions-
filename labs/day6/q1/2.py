import re
text = """
Hello, contact us at support@test.com.
You can also reach admin@company.co.in later.
"""

pattern=r"[a-zA-Z0-9._%+-]+@[a-zA_Z0-9.-]+\.[a-zA-z]{2,}"
match=re.search(pattern,text)
print(match.group())