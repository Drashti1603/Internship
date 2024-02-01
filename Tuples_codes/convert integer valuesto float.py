final_list = [] 
line = input("list of tuples:\n") 

while line != '':
    final_list.append(tuple(map(int, line.split())))
    line = input()

print("List of Tuples:", final_list) 
res = []
for tup in final_list:
    for ele in tup:
        res.append(float(ele))
 
# printing result 
print("Float: " + str(res))