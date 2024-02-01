lst1=[]
n=int(input("n =: "))
for i in range(0, n):
	ele=int(input())
	lst1.append(ele) 

lst=[]
for val in lst1:
    tup = (val, val**3)
    lst.append(tup)
print(lst)