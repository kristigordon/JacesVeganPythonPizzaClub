# JacesVeganPythonPizzaClub

This is an automatic pizza ordering program. 

There are 3 different sizes: Small. Medium, and Large.

And 2 options for toppings: Peperoni and Extra Cheese. 

Adding Pepperoni for Small is less than adding Pepperoni to a Meduim and Large. 
```
Here are the instructions:
Based on a user's order, work out their final bill.

Small Pizza: $10
Medium Pizza: $12
Large Pizza: $14
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $2
```

And here is my solution:

```
print("Welcome to Jace's Vegan Python Pizza Club")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0

if size == "S":
    bill += 10
elif size == "M":
    bill += 12
else:
    bill += 14

if add_pepperoni == "Y":
    if size == "S":
    bill += 2
    else:
    bill += 3

if extra_cheese == "Y":
    bill += 2

print(f"Your bill is: ${bill}")
```
<img width="889" alt="Screen Shot 2022-07-24 at 4 59 56 PM" src="https://user-images.githubusercontent.com/66803124/180665655-a69c5a0b-cefb-46f1-b9ff-a2cdad19a168.png">

Thank you!
