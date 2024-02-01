final_list = [] 
line = input("list of tuples:\n") 

while line != '':
    final_list.append(tuple(map(int, line.split())))
    line = input()

print("List of Tuples:", final_list)

mod = [abs(x % y) for x, y in final_list]

print("Tuple:", final_list)
print("Modulo:", mod)
