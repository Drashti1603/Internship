tup1 = tuple(input('Enter elements: ').split())
tup=list(tup1)
lst = len(tup)
for i in range(0, lst):
 
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
print(tup)