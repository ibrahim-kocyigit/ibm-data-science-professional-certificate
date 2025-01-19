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

### Freq function practice


def freq(string):
    words = string.lower().split()
    dict = {}

    for word in words:
        dict[word] = words.count(word)

    return dict


test = "Hello Ibrahim and hello Aykut. Today is Thursay and tomorrow is friday."

print(freq(test))

###
len(sum([1, 1, 2]))
len([sum([1, 1, 1])])

### string punctuation
import string

my_str = "Hello, World!"
clean = "".join([char for char in my_str if char not in string.punctuation])
print(clean)


###
class TextAnalyzer(object):
    def __init__(self, text):
        self.text = text.lower()
        self.fmtText = "".join(
            [char for char in self.text if char not in string.punctuation]
        )

    def freqAll(self):
        words = self.fmtText.split()
        freqMap = {}
        for word in set(words):
            freqMap[word] = words.count(word)
        return freqMap

    def freqOf(self, word):
        dct = self.freqAll()
        if word.lower() in dct.keys():
            return dct[word.lower()]
        else:
            return 0


ta = TextAnalyzer(my_str)
ta.freqOf("Hello")
ta.freqOf("world")
ta.freqOf("ibrahim")
