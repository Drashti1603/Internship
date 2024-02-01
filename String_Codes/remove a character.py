string = input("main string:")
x=input("char to be removed:")
result=" "
for char in string:
    if char != x:
        result += char
print(result)

