final_list = [] 
line = input("list of tuples:\n") 

while line != '':
    final_list.append(tuple(map(int, line.split())))
    line = input()

print("List of Tuples:", final_list) 
k = int(input("enter k:\n"))

div = []
for (x,y) in final_list:
	if x%k==0:
		div.append(x)
	if y%k==0:
		div.append(y)	
print("Tuple:", final_list)
print("Divisible:", div)