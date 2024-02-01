import re
strg=input("Enter string:")
x = re.findall("[a-z]", strg)
print(len(x))
y = re.findall("[A-Z]", strg)
print(len(y))
