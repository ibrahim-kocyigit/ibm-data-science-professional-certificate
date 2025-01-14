import re

s1 = "Michael Jackson is the best"

pattern = r"Jackson"

result = re.search(pattern, s1)

if result:
    print("Match found!")
else:
    print("No match")

pattern = r"\d\d\d\d\d\d\d\d\d\d"

text = "My number is 1234567890"

match = re.search(pattern, text)

if match:
    print(f"Phone number found: {match.group()}")
else:
    print("No match")
