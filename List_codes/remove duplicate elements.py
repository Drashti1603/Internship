lst1=[]
n=int(input("n =: "))
for i in range(0, n):
	ele=int(input())
	lst1.append(ele)
       
lst2 = set()

for word in lst1:
    if word not in lst2:
            print(word, end=" ")
            lst2.add(word)