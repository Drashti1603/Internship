final_list = [] 
line = input("list of tuples:\n") 

while line != '':
    final_list.append(tuple(map(int, line.split())))
    line = input()

print("List of Tuples:", final_list) 
freq = {}
for i in final_list:
    for elem in i:
        if elem in freq:
            freq[elem] += 1
        else:
            freq[elem] = 1

print("Frequency:", freq)