import random
deck = ["rock", "paper", "scissors"]
start_game = (input("Would like play rock-paper-scissors game now, yes or no?\n")).lower()

while start_game == 'yes':
    user_shoot = input("What are going to shoot this run, rock, paper, or scissors?\n").lower()
    user_shoot_index = deck.index(user_shoot)
    computer_shoot_index = random.randint(0, 2)
    computer_shoot = deck[computer_shoot_index]
    print(f"Here is the computer shoot:\n{computer_shoot}")

    if user_shoot == computer_shoot:
        print ("You won a draw.")
    else:
        if user_shoot_index < 2:
            if user_shoot_index < computer_shoot_index:
                print("You lose.")
            else:
                print("You won.")  
        else:
            if computer_shoot_index == 0:
                print("You lose.")
            else:
                print("You won.")

    start_game = (input("Game over. Play again, yes or no?\n")).lower()
