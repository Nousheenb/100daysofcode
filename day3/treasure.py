#treasur game just using if-else statements


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


cond1 = input('''You're at cross road.Where do you want to go? Type "left" or "right" ''')

if cond1 == "left" :
    cond2 = input('''You come to a lake.There is an island in the middle of the lake.Type "swim" to swim and "wait" to   wait.''')
    if cond2 == "wait":
        cond3 = input('''You arrived at the island unharmed.There is a house with three doors.One red , One yellow and one blue.Which colour do you choose? ''')
        if cond3 == "blue" :
            print("Eaten by beasts Game Over.")
        elif cond3 == "red":
            print("Burned by fire.Game Over")
        elif cond3 == "yellow":
            print("You win")
        else :
            print("Game over")
    else:
        print("Attacked by trout Game over.")


else :
    print("You fall into a hole Game Over.")
