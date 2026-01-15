import random

item_list = ["Rock","Paper","Scissors"]

computer_choice = random.choice(item_list)
user_choice = (input("Enter your Choice (Rock / Paper / Scissors) : "))

print (f" Your choice - {user_choice} , Computer's Choice - {computer_choice}")

if computer_choice == user_choice:
    print (" Both choices Matches - Match Tie")
elif computer_choice == "Rock" and user_choice == "Paper":
    print (" You WIN ")
elif computer_choice == "Rock" and user_choice == "Scissors":
    print (" Computer WINs ")
elif computer_choice == "Scissors" and user_choice == "Paper":
    print (" Computer WINS ")
elif computer_choice == "Scissors" and user_choice == "Rock":
    print (" You WIN ")
elif computer_choice == "Paper" and user_choice == "Scissors":
    print (" You WIN ")
elif computer_choice == "Scissors" and user_choice == "Rock":
    print (" You WIN ")
elif computer_choice == "Paper" and user_choice == "Rock":
    print (" Computer WINS ")