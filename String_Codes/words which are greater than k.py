
x = input("string:")
k = int(input("length:"))
list = []
s = x.split() 

for word in s:
    if len(word) > k:
        list.append(word)

print(list)
