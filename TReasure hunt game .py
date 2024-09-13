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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("you have passed the grand line , welcome to new world ")
print("the grand line is consisted to the east blue lake , where you will find the great treasure left by the pirate king somay THE ONE PIECE ")
print("How do you want to cross the lake? type wait for waiting for a boat , swim\n")
choice=input("How do you plan to cross the lake type wait , swim\n").lower()
if choice=="swim":
    print("GAME OVER! You Died Because the Sea was poisoned")
else:

   choice2= input("you have come to Laugh tale, There  is a crossroad , where wado you want to go "
          "type left , right\n").lower()

   if choice2=="left":
    print(" Game over! you were eaten by a wild dragon")
   else:
       choice3=input("NOW you have entered the sacred temple of IMU. But there are 3 doors and "
                     "one of the doors holds the great treasure THE ONE PIECE "
                     " Type red, yellow,blue to open the gate\n").lower()
       if choice3=="yellow":
           print("Congratulations you found the Great Treasure THE ONE PIECE ")
       elif choice3=="red":
           print("Game over! the Room which you chose was already set on fire ")
       elif choice3=="blue":
           print("Game over! the Door you chose was keeping Lord IMU hungry pet")
































