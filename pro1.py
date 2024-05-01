import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll      #this is just a random number generator between a max value and a min value 

# value = roll()
# print(value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():              #if it's not a digit then obviously we will terminate 
        players = int(players)         #the program with a invalid error sign
        if 2<=players<=4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again")             #this whole block of code is written to
                                                #define the actual player count ensuring it to be between 2 and 4 inclusively

# print(players)

max_score = 25
player_scores = [0 for _ in range(players)]    #return [0,0,0] like this

# print(player_scores)

while max(player_scores) < max_score:

    for player_i in range(players):
        print("\nPlayer",player_i + 1,"turn has just started\n")
        print("your total score is: ",player_scores[player_i],"\n")
        count = 0

        while True:
            should_roll = input("Would you like to roll? (y): ")
            if should_roll.lower() == "y":
                value = roll()
            else:
                break

            if value == 1:
                print("You rolled 1! Your turn is over")
                count = 0
                break
            else:
                count+=value
                print("you rolled a: ", value)

            print("your score is : ",count)
        
        player_scores[player_i] += count
        print("Your total score is: ", player_scores[player_i])

max_score = max(player_scores)
winning_i = player_scores.index(max_score)
print("Player ", winning_i+1, "is the winner with a score of : ",max_score)