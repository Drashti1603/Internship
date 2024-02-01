lst1=[]
n=int(input("n =: "))
for i in range(0, n):
	ele=int(input())
	lst1.append(ele) 

even=[]
odd=[]
for i in lst1:
	if i%2==0:
		even.append(i)
	else:
		odd.append(i)
print(even)
print(odd)