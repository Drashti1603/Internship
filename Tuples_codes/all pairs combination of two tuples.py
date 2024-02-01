lst1=[]
n=int(input("n =: "))
for i in range(0, n):
	ele=int(input())
	lst1.append(ele) 

print(lst1)
lst2=[]
n=int(input("n =: "))
for i in range(0, n):
	ele=int(input())
	lst2.append(ele) 

print(lst2)
str(lst1)
str(lst2)
res = [(a, b) for a in lst1 for b in lst2] + [(a, b) for a in lst2 for b in lst1]
print("All pair combinations of 2 tuples : " + str(res))
