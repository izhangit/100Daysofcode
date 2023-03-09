
# Continue

while True:
    print("You are in a coridoor, do you go left or right?")
    direction = input("> ")
    if direction == "left":
        print("You have fallen to your death")
        break
    elif direction == "right":
        continue
    else:
        print("Ahh! You're a genius, you,ve won")
        exit()
print("The game is over, you're failed!")