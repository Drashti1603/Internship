lst=[]
n=int(input("n =: "))
for i in range(0, n):
	ele=int(input())
	lst.append(ele) 
print(lst)
sqr = [i ** 2 for i in lst] 
cube = [i ** 3 for i in lst] 
print(sqr)
print(cube)

