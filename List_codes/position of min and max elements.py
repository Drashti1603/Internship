lst1=[]
n=int(input("n =: "))
for i in range(0, n):
	ele=int(input())
	lst1.append(ele) 

print(lst1)
min=lst1.index(min(lst1))
max=lst1.index(max(lst1))

print("max position", max+1)
print("min position", min+1)