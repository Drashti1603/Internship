##Program 3###
lst = []
 
n = int(input("Elements : "))
 
for i in range(0, n):
    ele = str(input())
    lst.append(ele) 

s = " ".join(lst)
count=0
i=0
for char in s:
  if (char=='a'or char=='e'or char=='i'or char=='o'or char=='u'or char=='A'or char=='E'or char=='I'or char=='O'or char=='U'): 
    count+=1
print(count)