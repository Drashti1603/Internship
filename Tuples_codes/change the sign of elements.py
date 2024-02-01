final_list = [] 
line = input("list of tuples:\n") 

while line != '':
    final_list.append(tuple(map(int, line.split())))
    line = input()

print("List of Tuples:", final_list) 
change = []
for (x,y) in final_list:
	if x>0:
		change.append(-abs(x))
	else:
		change.append(abs(x))
	if y>0:
		change.append(-abs(y))
	else:
		change.append(abs(y))
	if x==y:
		change.append(x)	
print("Tuple:", final_list)
print("change signs:", change)