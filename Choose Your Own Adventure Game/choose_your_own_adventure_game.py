name = input("Enter your name: ")
print(f"Welcom {name} to this adventure!")

print("You are going on an unknown adventure. You walked to a dirt road. There are two ways, right and left. Which way are you going?")
answer = input("Left or Right? : ").lower()

if answer == "left":
    print("You walked the left way and found yourself on a river side. There are two ways, over the bridge or swim the water.")
    answer = input("Bridge or swim? : ").lower()
    if answer == "bridge":
        print("Bridge was pretty old. The bridge broke and you die, YOU LOSE!")
    elif answer == "swim":
        print("You swam across the river but now you are wet. You see a strangers house.")
        answer = input("Talk or Ignore? : ").lower()
        if answer == "talk":
            print("They killed you. YOU LOSE!")
        elif answer == "ignore":
            print("You ignored them, they are offended and killed you. YOU LOSE!")
        else:
            print("Invalid Input. YOU LOSE!")
    else:
        print("Invalid Input. YOU LOSE!")

elif answer == "right":
    print("You walked the right way and found yourself in a jungle. You hear  some noise coming from the bushes. You wanna check it or not?")
    answer = input("Check or Ignore : ").lower()
    if answer == "check":
        print("You checked the noise and accidentally found gold, YOU WIN!")
    elif answer == "ignore":
        print("You Ignored the noise and it was a bear, it killed you. YOU LOSE!")
    else:
        print("Invalid Input. YOU LOSE!")

else:
    print("Invalid Input. YOU LOSE!")