import random
user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissor']
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quite: ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        print("Not Available !")
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    print(f"Computer Picked {computer_pick}")

    if user_input == "rock" and computer_pick == "scissor":
        print("You win  😄  😄 !")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You win  😄  😄 !")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("You win")
        user_wins += 1
    else:
        print("You loss! Computer win !")
        computer_wins += 1

print(f"You win {user_wins} times")
print(f"Computer wins {computer_wins} times")
print("Goodbye! ")