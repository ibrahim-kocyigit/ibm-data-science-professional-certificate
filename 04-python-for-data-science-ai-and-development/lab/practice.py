import re

###
s1 = "Michael Jackson is the best"
pattern = r"Jackson"
result = re.search(pattern, s1)

if result:
    print("Match found!")
else:
    print("No match")

###
pattern = r"\d\d\d\d\d\d\d\d\d\d"
text = "My number is 1234567890"
match = re.search(pattern, text)

if match:
    print(f"Phone number found: {match.group()}")
else:
    print("No match")

###
pattern = r"\W"  # any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)
print("Matches: ", matches)

###
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
result = re.findall("as", s2)
print(result)

# \s - Matches any whitespace character (space, tab, newline, etc.)
split_array = re.split(r"\s", s2)
print(split_array)

# We can manipulate a list nested in a tuple...
tuple = (1, 2, ["a", "b"])
tuple[2][0] = "c"
tuple

# ... But we cannot manipulate a tuple nested in a list
list = [1, 2, ("a", "b")]
list[2][0] = "c"  # Raises a TypeError: 'tuple' object does not support item assignment

help(list)

###
