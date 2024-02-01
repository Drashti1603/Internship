def swap(str, i, j):
   list1 = list(str)
   list1[i], list1[j] = list1[j], list1[i]
   return ''.join(list1)

string = input("main string:")
x=int(input("1st postion to be swapped:"))
y=int(input("2nd postion to be swapped:"))
print(swap(string, x, y))