import random
top_of_range = input("Type a number ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number less then 0 next time")
        quit()
else:
    print("Type a Top range number ")
    quit()
random_number = random.randint(1, top_of_range)
user_guess = None
guess = 0
while True:
    guess += 1
    print(f"Please guess the number between 1 to {top_of_range} ")
    user_guess = input("Enter number ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            print("You are win  💪  💪  😺  😺 ")
            break
        else:
            print("You are not win  😭  😭  😭 ")
    else:
        print("Please type a number next time")
        continue

    print(f"Your random number is {random_number}")
    print(f"Your Guess number is {user_guess}")

print(f"Your random number is {random_number}")
print(f"Your Guess number is {user_guess}")
print(f"Total hit number {guess}")
print("Game Over !")