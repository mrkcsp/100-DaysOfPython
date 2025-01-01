print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")

direction = input("There is a crossroad. You wanna go left or right? ").lower()
if direction == "left":
    choice = input("There is a lake. You wanna 'wait' for a boat or 'swim'? ").lower()
    if choice== "wait":
        door = input("Choose one of the 'blue' or 'yellow' or 'red' door you find on the little island: ").lower()
        if door == "yellow":
            print("You found the TREASURE! You Win!")
        else:
           print("Game Over. Nothing inside")

    else:
          print("Game Over. A crocodile eat you...")

else:
        print("Game Over. You find a zombie and you're unarmed!")

