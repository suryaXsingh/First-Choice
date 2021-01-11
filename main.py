name = input("Enter Your Name = ")
age = int(input("Enter Your Age = "))


if age>=13:
    print("Hello" ,name)    
    print('''Welcome To First Choice.
Result of the game depends on your Choices.
So be careful at your First Choice.''')
    print("You Need to find you FAMILY TREASURE to Win.")

    direction = input("In what direction do you want to go? (left/right) ").lower()

    if direction=="right":
        print("Right is not always the right way!")
    elif direction=="left":
        print("You walked left and found a MONSTER.")

        monster = input(print("Do you want to fight or run? (fight/run) ")).lower()
        if monster=="fight":
            print("You took the fight with MONSTER but MONSTER was so strong. \n So he killed you")
        elif monster=="run":
            print("You ran away from MONSTER and saved your life.")

            option = input(print("You saw a Old School and a House. Where do you want to go? (school/house)")).lower()
            if option=="school":
                print("The School was to old. \nSo you entered the school and the school roof fell on you. \nRIP")
            elif option=="house":
                print("It was your old family house and you found your FAMILY TREASURE. \nAnd Now You are a BILLIONAIRE because of your Right Choices. \nSo always be careful at your FIRST CHOICE")
            else:
                print("You lost because you typed wrong option!")


        else:
            print("You lost because you typed wrong option!")
    else:
        print("You lost because you typed wrong option!")
else:
    print("Hello" ,name ,"You are not old enough to play this game.")
