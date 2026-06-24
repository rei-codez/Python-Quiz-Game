print("Welcome to the Quiz Game!")
playing = input("Do you want to play?: ").lower()
if playing == "yes":
    print("Great! Let's start the game.")
else:
    quit()

score = 0
answer = input("Who built Python? ")
if answer.lower() == "guido van rossum":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Python was built by Guido van Rossum.")

answer = input("What are binary numbers? ")
if answer.lower() in ["0 and 1", "0s and 1s", "0,1"]:
    print("Correct!")
    score += 1
else:
    print("Incorrect! Binary numbers are represented using only 0s and 1s.")
answer = input("In which year was Python created? ")
if answer.lower() == "1991":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Python was created in 1991.")

answer = input("What was python named after? ")
if answer.lower() == "monty python's flying circus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!Python was named after Monty Python's Flying Circus.")

answer = input("How many versions of Python are there? ")
if answer.lower() == "3":
    print("Correct!")
    score += 1
else:
    print("Incorrect! There are currently 3 major versions of Python.")

print("You got " + str(score) + " out of 5 questions correct!")
print(str(score/5 * 100) + "%.")
