x = input("Enter Str1: ")
y = input("Enter Str2: ")

s1 = sorted(x)
s2 = sorted(y)

if s1 == s2:
    print("Is anagram")
else:
    print("Is not anagram")
