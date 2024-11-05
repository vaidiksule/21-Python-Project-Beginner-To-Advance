import random as rd

print("1-Stone \n 2-Paper \n 3-Scissor \n ")

no_of_rounds = int(input("Enter no of rounds: "))

comp_score = 0
user_score = 0

current_round = 1
while current_round <= no_of_rounds:
    print("Round ", current_round)

    user_choice = int(input("Enter Your Choice: "))
    comp_choice = rd.randint(1,3)

    if  0 < user_choice < 4:
        current_round += 1

        if user_choice == 1:
            if comp_choice == 2:
                print("Computer Won!")
                comp_score += 1
            elif comp_choice == 3:
                print("You Won!")
                user_score += 1
            else:
                print("Draw!")

        elif user_choice == 2:
            if comp_choice == 1:
                print("You Won!")
                user_score += 1
            elif comp_choice == 3:
                print("Computer Won!")
                comp_score += 1
            else:
                print("Draw!")

        elif user_choice == 3:
            if comp_choice == 1:
                print("Computer Won!")
                comp_score += 1
            elif comp_choice == 2:
                print("You Won!")
                user_score += 1
            else:
                print("Draw!")

        else:
            print("Enter a number between 1 to 3")
        print("*" * 20)

    else: 
        print("Please Enter Valid Choice.")

print("Your Score: ", user_score)
print("Computer Score: ", comp_score)

if user_score > comp_score:
    print("#"*10)
    print("YOU ARE THE WINNER")
    print("#"*10)
else:    
    print("#"*10)
    print("COMPUTER IS THE WINNER")
    print("#"*10)