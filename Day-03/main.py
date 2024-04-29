print("welcome to treasure island")
print ("your mission is to find the treasure")
choice1 = input('you\'re at a crossroad, where do you want to go? Type Left or Right ').lower()
if choice1 == "left":
    choice2 = input('you have come into a lake. there is an island in the middle of the lake. type "wait" or type "swim" to swim accross.').lower()
if choice2 == "wait":
    choice3 = input('you arrive the highland unharmed, There is a house with 3 door one red, one blue, one yellow which colour do you choose').lower()
    if choice3 == "red":
        print('its a room full of fire: Game Over')
    elif choice3 =="yellow":
        print("congratulation you found the treasure")
    elif choice3 ==" blue":
        print("you enter a room full of beast: Game Over")
    else:
        print("you enter the room that doesnt exist: game over")
else:
    print("you fell into a hole, Game Over")