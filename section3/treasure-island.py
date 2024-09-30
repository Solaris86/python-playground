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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road_choice = input("You are at the crossroads. "
                    "Where do you want to go? "
                    "Left or right? ").lower()
if road_choice == "left":
    print("You come upon the river. "
          "There is no bridge. "
          "What will you do?")
    river_choice = input("Swim or wait? ").lower()
    if river_choice == "wait":
        print("A boat comes that transfers you safely across the river. "
              "In the distance you a see a castle.")
        print("Upon arriving at the castle you see three doors, red, yellow and blue.")
        door_choice = input("Which one do you choose? ").lower()
        if door_choice == "yellow":
            print("You win!")
        elif door_choice == "red":
            print("Burned by fire! Game over!")
        elif door_choice == "blue":
            print("Eaten by beasts! Game over!")
        else:
            print("Game over!")
    else:
        print("Attacked by a trout! Game over!")
else:
    print("You fell into a whole! Game over!")