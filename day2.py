#tip calculator

print("Welcome to tip calulator")

bill = float(input("What's the total bill? "))
tip_per = int(input("What percentage of tip?(10 ,12 or 15) "))
people = int(input("How many people to split? "))

tip =  bill *( tip_per/ 100 )

per_person_amt = bill / people

amt  = per_person_amt + tip 

print(f"Each person should pay: {amt}")
