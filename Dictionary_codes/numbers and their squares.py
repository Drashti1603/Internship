list1 = []
n1 = int(input("Enter the number of elements for list 1: "))
for i in range(0, n1):
    ele = int(input())
    list1.append(ele)
list2 = []
for i in list1:
    ele = i**2
    list2.append(ele)
print("Num : " + str(list1))
print("Square : " + str(list2))
res = {}
for key in list1:
	for value in list2:
		res[key] = value
		list2.remove(value)
		break

print("Resultant dictionary is : " + str(res))
