def addition(n1, n2):
    return n1 + n2

def subtra(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

print("Select Operations")
print(
    "1. Addition\n"
    "2. Subtra\n"
    "3. Multiplication\n"
    "4. Division\n")

operation = int(input("Enter choice of operation 1/2/3/4: "))
n1 = int(input("Enter the First Number: "))
n2 = int(input("Enter the Second Number: "))

if operation == 1:
    print (addition(n1, n2))
elif operation == 2:
    print (subtra(n1, n2)) 
elif operation == 3:
    print (multiplication(n1, n2))   
elif operation == 4:
    print (division(n1, n2))    
else:
    print("Invalid Input")