print("Welcome to PYTHON PIZZA deliveries!")
print("Place your Order")

size  = input("What size of pizza Do you want?(S / M / L) ")
bill =0 


if size == "S":
    bill += 15
    pepporini = input("Do you want pepporini? Y or N ")
    if pepporini == "Y":
        bill += 2

elif size == "M":
    bill += 20
    pepporini = input("Do you want pepporini? Y or N ")
    if pepporini == "Y":
        bill += 3
    
elif size == "L":
    bill += 25
    pepporini = input("Do you want pepporini? Y or N ")
    if pepporini == "Y":
        bill += 3
        
extra_cheese = input("Do you want some extra cheese? Y or N ")

if extra_cheese == "Y":
    bill += 1
    
    
print(f"Your final bill is ${bill}")
