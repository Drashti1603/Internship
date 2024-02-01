
###Program 4####
str_input = input("Enter a string: ")
str_list = list(str_input)

# Check if the string has at least two characters
if len(str_list) >= 2:
    temp = str_list[0]
    str_list[0] = str_list[-1]
    str_list[-1] = temp

    modified_str = ''.join(str_list)
    print(modified_str)
else:
    print("String has less than two characters, no swap performed.")
# for i in str ## e=i+e ---- Way 2
# reversed function ----- way 3