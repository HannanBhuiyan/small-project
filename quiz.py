print("Welcome to our programming quiz ")
playing = input("Do you want to play? ")

if playing != "yes":
    print("Quiz Closed !")
    exit()
print("Okay ! let's play :)")

score = 0

ans = input("What does HTML stand for? ")
if ans == "hyper text markup language":
    print("Correct !")
    score += 1
else:
    print("Wrong !")

ans = input("What does PHP stand for? ")
if ans == "hyper text pre processor":
    print("Correct !")
    score += 1
else:
    print("Wrong !")

ans = input("What does CSS stand for? ")
if ans == "cascading style sheets":
    print("Connect !")
    score += 1
else:
    print("Wrong !")

print(f"You got {score} question correct")

# result = ((score / 3) * 100)
# text = "You got {:.2f} %"
# print(text.format(result))

print("You got {:.2f} %".format((score / 3) * 100))



