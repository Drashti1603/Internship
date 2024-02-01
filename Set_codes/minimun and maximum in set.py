#initialize the set
my_set = {5, 2, 8, 1, 9, 2, 18}

# Convert set to a list
list1 = list(my_set)

n = len(list1)
for i in range(n-1):
    for j in range(0, n-i-1):
        if list1[j] > list1[j + 1]:
             list1[j], list1[j + 1] = list1[j + 1], list1[j]
print(list1)
print("Min",list1[0])
print("Max",list1[n-1])
