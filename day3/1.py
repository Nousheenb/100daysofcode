#understanding conditionals - if and nested if 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
price = 0

if height >= 120:
  print("You can ride")
  age = int(input("What's your age? "))
  if age < 12:
    price  += 5
      
  elif age <= 18:
    price  += 7

  else:
    price  += 12

  flag = input("Do you want a picture?(Y/N) ")
  if flag == 'Y':
    price += 3

  print(f"You should pay ${price}.")
else:
  print("You can't ride")
