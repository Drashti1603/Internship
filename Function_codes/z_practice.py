if 5 > 2:
  print("Five is greater than two!")
"""
This is a comment
written in
more than just one line
"""
x = str(5)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(type(x))
print(type(y))


x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

########################################
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#####################################
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#########################################
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

x = "aww"

print("Python is " + x)
###########################################
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
################################
for x in "banana":
  print(x)
#######3############
txt = "The best things in life are free!"
print("free" in txt)

#swap frist and end item
fruits=["apple","orange","strawberry"]
print(fruits)

def swap():
    temp=fruits[0]
    fruits[0]=fruits[2]
    fruits[2]=temp
    print(fruits)

swap()
    
###################################################
#format() function
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
######################################################
#print ""  in python
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#####################################################
#String methds
txt = "hello, and welcome to my world."

x = txt.encode()

print (x)
