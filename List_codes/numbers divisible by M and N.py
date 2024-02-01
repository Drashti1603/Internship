lst=[]
n=int(input("n =: "))
for i in range(0, n):
	ele=int(input())
	lst.append(ele) 

m=int(input("Enter num1:"))
n=int(input("Enter num2:"))
lst1=[]
for i in lst:
	if i%m==0 or i%n==0:
		lst1.append(i)
print(lst1)