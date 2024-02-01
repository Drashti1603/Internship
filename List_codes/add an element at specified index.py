lst = []
n = int(input("n =: "))
for i in range(0, n):
	ele = int(input())
	lst.append(ele) 

print(lst)
x=int(input("index:"))
v=int(input("value:"))
lst.insert(x,v)
print(lst)