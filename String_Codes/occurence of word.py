x=input("string:")
list={}
s=x.split(" ") 
for words in s:
    if words in list:
        list[words] += 1
    else:
        list[words] = 1
 
print(str(list))
