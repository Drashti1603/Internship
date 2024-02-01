list1 = []
n1 = int(input("Enter the number of elements for list 1: "))
for i in range(0, n1):
    ele = int(input())
    list1.append(ele)

print("List 1:", list1)

list2 = []
n2 = int(input("Enter the number of elements for list 2: "))
for i in range(0, n2):
    ele = int(input())
    list2.append(ele)

print("List 2:", list2)

list3 = []
n3 = int(input("Enter the number of elements for list 3: "))
for i in range(0, n3):
    ele = int(input())
    list3.append(ele)

print("List 3:", list3)
def find_common(list1, list2, list3):

	set1 = set(list1)
	set2 = set(list2)
	set3 = set(list3)
	return [elem for elem in set1 if elem in set2 and elem in set3]



common = find_common(list1, list2, list3)
print(common)
