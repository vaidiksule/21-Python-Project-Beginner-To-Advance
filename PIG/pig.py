import random as rd

def roll():
    return rd.randint(1,6)

while True:
    no_of_players = input("Enter the no of Players(2/4): ")
    if no_of_players.isdigit():
        no_of_players = int(no_of_players)
        if 1 < no_of_players < 5:
            break
    print("Must be between 2 to 4 players")

max_score = 30
players_score = [0 for _ in range(no_of_players)]  # if no of players = 3 ---> [0, 0, 0]

while max(players_score) < max_score:
    for player_index in range(no_of_players):
        print("===================================")
        print(f"Player {player_index + 1} turn! \n")
        current_score = 0

        while True:
            should_roll = input("do you want to roll the dice (y)? ")
            if should_roll.lower() != 'y':
                break
            
            value = roll()

            if value == 1:
                print("You Rolled 1, ELIMINATED!")
                current_score = -(players_score[player_index])
                break
            else:
                current_score += value
                print(f"You Rolled {value}")
                
            print("Your Score is: ", current_score)
            
        players_score[player_index] += current_score
        print("Your Total Score is: ", players_score[player_index])
winning_index = players_score.index(max(players_score))
print("***************************************")
print(f"Player {winning_index + 1} WON!")
print("***************************************")
