x = input("Enter Str1: ")
y = input("Enter Str2: ")

s1 = sorted(x)
s2 = sorted(y)
for i in s1:
   if i in s2:
        print("Is not disjoint")
        break
   else:
        print("Is disjoint")
        break
