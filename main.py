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