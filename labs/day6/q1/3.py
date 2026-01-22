import re

text = "Big Brother is 21 years old"

# 1) .  → any one character
print(re.findall(r"B.g", text))      
# ['Big']

# 2) * → zero or more
print(re.findall(r"o*", text))       
# matches '', 'o', 'oo' etc.

# 3) + → one or more
print(re.findall(r"o+", text))       
# ['o', 'oo']

# 4) ? → optional
print(re.findall(r"colou?r", "color colour"))  
# ['color', 'colour']

# 5) \d → digits
print(re.findall(r"\d+", text))      
# ['21']

# 6) \w → word characters
print(re.findall(r"\w+", text))      

# 7) \s → spaces
print(re.findall(r"\s", text))       
