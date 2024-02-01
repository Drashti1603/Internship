lst = []
n = int(input("n =: "))
for i in range(0, n):
	ele = int(input())
	lst.append(ele) 

print(lst)
del lst[0: 2]
print(lst)
##
start = int(input("start =: "))
end = int(input("end =: "))
new_lst = [i for i in lst if i < start or i > end]

print(new_lst)
	
