lst1=[]
n=int(input("n =: "))
for i in range(0, n):
	ele=int(input())
	lst1.append(ele) 

print(lst1)
k = int(input('Enter k: '))
res = [ele for ele in lst1 if len(ele) != k]

print(res)