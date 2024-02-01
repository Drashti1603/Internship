list1 = []
n1 = int(input("Enter the number of elements for list 1: "))
for i in range(0, n1):
    ele = input()
    list1.append(ele)

print("List 1:", list1)

list2 = []
n2 = int(input("Enter the number of elements for list 2: "))
for i in range(0, n2):
    ele = int(input())
    list2.append(ele)

print("List 2:", list2)

print("Original key list is : " + str(list1))
print("Original value list is : " + str(list2))


res = {}
for key in list1:
	for value in list2:
		res[key] = value
		list2.remove(value)
		break

print("Resultant dictionary is : " + str(res))
