final_list = [] 
line = input("list of tuples:\n") 

while line != '':
    final_list.append(tuple(map(int, line.split())))
    line = input()

print("List of Tuples:", final_list)
ind = []
for (x,y) in final_list:
	if x%2==0:
		ind.append(x)
	if y%2==0:
		ind.append(y)	
print("Tuple:", final_list)
print("index values:", ind)