lst=[]
n=int(input("n =: "))
for i in range(0, n):
	ele=input()
	lst.append(ele) 

print(lst) 
res = []
for sub in lst:
    if res and res[-1][0] == sub[0]:
        res[-1].extend(sub[1:])
    else:
        res.append([ele for ele in sub])
res = list(map(tuple, res))
print("The extracted elements : " + str(res))