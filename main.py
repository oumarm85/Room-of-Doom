print('''
*******************************************************************************
                             ^
                _______     ^^^
               |xxxxxxx|  _^^^^^_
               |xxxxxxx| | [][]  |
            ______xxxxx| |[][][] |
           |++++++|xxxx| | [][][]|
           |++++++|xxxx| |[][][] |
           |++++++|_________ [][]|
           |++++++|=|=|=|=|=| [] |
           |++++++|=|=|=|=|=|[][]|
___________|++HH++|  _HHHH__|   _________   _________  _________
         _______________   ______________      ______________
__________________  ___________    __________________    ____________
*******************************************************************************
''')
print("Welcome to the Room of Doom!")
print("Your mission is to escape.")

door = input("You wake up in a strange room and there are two doors infront of you, which do you take? Left or Right?\n")

door = door.lower()

if door == "left":
  travel = input("As you walk to the end of the corridor, you come across some stairs and a elevator. Do you take the Stairs or Elevator?\n")
  travel = travel.lower()

  if travel == "stairs":
    exit = input("As you make your way to the ground floor, you come across 3 doors with lights behind them. Do you take the Green, Red or Blue door?\n")

    exit = exit.lower()

    if exit == "red":
      print("The red door had a horde of zombies waiting for you, who attached you and you turned into a zombie. GAME OVER!")
    elif exit == "green":
      print("The green door is a room full of fire, where you burn to death. GAME OVER!")
    elif exit == "blue":
      print("You successfully exit what appears to be a hospital, and are free. CONGRATULATIONS YOU WON! (the next challenge will be getting home safe and sound!)")
    else:
      print("The door you selected does not exist. Turns out you are crazy and a nurse finds you and takes you back to your room. GAME OVER!")

  else:
    print("The elevator malfuntioned and you crashed to your death. GAME OVER!")

else:
  print("As you walk through the door you fall 10 stories to your death. GAME OVER!")
