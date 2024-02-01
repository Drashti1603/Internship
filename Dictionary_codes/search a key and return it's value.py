dict = {"Java": 100, "Python": 112, "C": 11}
x = input("Enter a value: ")

for key, value in dict.items():
    if x == str(value): 
        print(key)
        break
else:
    print("Value not found")
