import re

# pattern = re.compile(r"([a-zA-z]).([a])")
# string = "search this inside of this text please!"

# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)

# print(a.group())
# print(b)
# print(c)
# print(d)

# password - at least 8 characters, contain letters, numbers, $%#@
pattern = re.compile(r"([a-zA-Z0-9\$\%\#\@]{8,}")
string = "enterpassword"
a = pattern.search(string)
print(a)
