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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

cross_road=input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")

if cross_road.lower()=="left":
          lake=input("You have now come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
else:
          print("You fell into a hole and now you are dead")
          print("GAME OVER")
          exit()
if lake.lower()=="wait":
          house=input("You arrived at the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which color do you choose?\n")
else:
          print("You were Attacked by sharks")
          print("GAME OVER")
          exit()

if house.lower()=="yellow":
          print("You made it !!!!!")
          print("YOU WIN MATE !!")
elif house.lower()=="red":
          print("You where burned by fire")
          print("GAME OVER")
          exit()
elif house.lower()=="blue":
          print("You where eaten by Beasts")
          print("GAME OVER")
          exit()
else:
           print("GAME OVER")
          
          
          
          

          
          
          
          

                 

