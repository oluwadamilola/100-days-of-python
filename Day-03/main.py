print("welcome to treasure island")
print ("your mission is to find the treasure")
choice1 = input('you\'re at a crossroad, where do you want to go? Type Left or Right ').lower()
if choice1 == "left":
    choice2 = input('you have come into a lake. there is an island in the middle of the lake. type "wait" or type "swim" to swim accross.').lower()
else:
    print("you fell into a hole, Game Over")