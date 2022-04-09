name = input("What is your name?")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to abn end and you can go right or left:")
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around or swim to swim across: ")
    if answer == 'swim':
        print("There was an alligator in the water. Game over.")
    elif answer == "walk":
        print("You walked 10 miles and ran out of water. Game over.")
    else:
        print("Not a valid answer. You lose. ")

elif answer == "right":
    answer = input("You see a bridge, it looks unsafe, do you wish to cross or return?")
    if answer == 'return':
        print("There was a killer waiting for you. Game over.")
    elif answer == "cross":
        answer = input("You have crossed the bridge and meet a stranger. Do you wish to talk to them? Enter yes or no: ")
        if answer == 'no':
            print("The stranger thinks you are rude and stabs you in the back")
        elif answer == "yes":
            print("Stranger gives you a million dollars and calls an uber for you to get home safely. But now they have your address muahahahahahahahaahaha!")
        else:
            print("Not a valid answer. You lose. ")
    else:
        print("Not a valid answer. You lose. ")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name)