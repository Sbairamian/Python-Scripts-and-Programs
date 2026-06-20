print(f"Computer chose {choice2}")

if choice1 == choice2:
    print("Draw")
elif choice1 == 0:
    if choice2 == 1:
        print("Rock loses to Paper. You lose :(")
    elif choice2 == 2:
        print("Rock beats Scissors. You win!")
elif choice1 == 1:
    if choice2 == 0:
        print("Scissors beats Rock. You win!")
    elif choice2 == 2:
        print("Paper loses to Scissors. You lose :(")
elif choice1 == 2:
    if choice2 == 0:
        print("Scissors loses to Rock. You lose :(")
    elif choice2 == 1:
        print("Scissors beats Paper. You win!")
else:
    print("Invalid input")

# elif choice1 == 2 and choice2 == 0:
#     print("Scissors loses to Rock. You lose")
# elif choice1 == 1 and choice2 == 0:
#     print("Paper beats rock.  You win!")
# elif choice1 == 0 and choice2 == 1:
#     print("Rock beats scissors.  You win!")
# elif choice1 == 1 and choice2 == 0:
#     print("Paper beats rock.  You lose!")
