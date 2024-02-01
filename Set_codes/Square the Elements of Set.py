list1 = []
n2 = int(input("Enter: "))
for i in range(0, n2):
    ele = int(input())
    list1.append(ele)

print("List:", list1)
st = set(list1)

squared_set = set()
for element in st:
    squared_set.add(element ** 2)

print("Original Set:", st)
print("Squared Set:", squared_set)
