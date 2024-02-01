lst=[]
n=int(input("n =: "))
for i in range(0, n):
	ele=int(input())
	lst.append(ele) 

print(lst)

tup=()
tup = tuple(input('Enter: ').split())


print(tup)
res = tuple(list(tup) + lst)
print(res)
