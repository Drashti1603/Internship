str1=input("main string:")
n = len(str1);  
subs = [];  
   
for i in range(0,n):  
    for j in range(i,n):  
        subs.append(str1[i:(j+1)]);  
   
print("All subsets: ");  
for i in subs:  
    print(i);  