lst=[]
n=int(input("n =: "))
for i in range(0, n):
	ele=int(input())
	lst.append(ele)
	 
for i in range(n-2):
	if lst[i] == lst[i + 1] and lst[i + 1] == lst[i + 2]:
		print("the commmon num:",lst[i])
