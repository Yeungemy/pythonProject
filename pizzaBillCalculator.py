# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == 'S':
  bill += 15
elif size == 'M':
  bill += 20
elif size == "L":
  bill += 25

if add_pepperoni == 'Y':
  bill += 2
if extra_cheese == 'Y':
  bill += 3

print("size = " + size)
print("add_pepperoni = " + add_pepperoni)
print("extra_chesse = " + extra_cheese)
print(f"Your final bill is: ${bill}")