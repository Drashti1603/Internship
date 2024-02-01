string = input("Main string: ")
string = string.lower()
vowels = set("aeiou")
s = set()

for char in string:
    if char in vowels:
        s.add(char)

if len(s) == len(vowels):
    print("Accepted")
else:
    print("Not Accepted")

	
