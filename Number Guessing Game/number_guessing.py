import random as rd

lower_limit = int(input("lower limit: "))
higher_limit = int(input("higher limit: "))
no_of_hints = int(input("No of hints: "))

number = rd.randint(lower_limit, higher_limit)
no_of_try = 0
previous_guess = 0

def hint():
    if number < previous_guess:
        print(f"your guess is higher.\n {no_of_hints} hints left")
    elif number > previous_guess:
        print(f"your guess is lower.\n {no_of_hints} hints left")

while True:
    no_of_try += 1
    guess = input("Enter your guess: ")
    if guess.lower() == "h":
        if no_of_hints != 0:
            no_of_hints -= 1
            no_of_try -= 1
            hint()
            continue
        else:
            no_of_try -= 1
            print("you used all your hints")
            continue

    if int(guess) == number:
        print("Correct! \n "f"You took {no_of_try} tries to guess!")
        break
    else:       
        previous_guess = int(guess)
        continue
