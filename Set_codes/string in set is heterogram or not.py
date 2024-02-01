string=input("main string:")
sorted_string = sorted(string.lower())
for i in range(1, len(sorted_string)):
    if sorted_string[i] == sorted_string[i-1] and sorted_string[i].isalpha():
        print("No")
        break
else:
    print("Yes")



