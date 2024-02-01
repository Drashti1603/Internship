import random
min_value=1
max_value=6
roll_again = "yes"
while roll_again == "yes":
    print("Rolling the dices...")
    print("The values are....")
    val1=random.randint(min_value, max_value)
    val2=random.randint(min_value, max_value)
    print(val1,val2)
    roll_again = input("type yes to roll the dices again.")
print("Have a good day.")