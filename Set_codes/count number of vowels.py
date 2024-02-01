string = input("Main string: ")
string = string.lower()
vowels = set("aeiou")
s = set()
count = 0

for char in string:
    if char in vowels:
        count += 1

print(count)

