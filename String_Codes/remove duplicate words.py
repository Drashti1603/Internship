x = input("string:")
list1 = set()
s = x.split(" ")

for word in s:
    if word not in list1:
            print(word, end=" ")
            list1.add(word)