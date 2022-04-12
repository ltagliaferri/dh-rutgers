# Where we ended on rock-paper-scissors in the last class session

# rock = 0
# paper = 1
# scissors = 2
# 0 > 2
# 1 > 0
# 2 > 1

print("Do you want to play Rock Paper Scissors?\nType 'y' for yes")

answer = input()

while answer.lower() == "y": 
    print("Enter 0 for Rock, Enter 1 for Paper, Enter 2 for Scissors")

    print("Player 1, enter your number: ")
    player_one = int(input())

    print("Player 2, enter your number: ")
    player_two = int(input())

    if player_one > 2 or player_two > 2:
        print("Out of bounds")
    elif player_one == player_two:
        print("Tie!")
    elif player_one == 0 and player_two == 1:
        print("Player two wins.")
    elif player_one == 0 and player_two == 2:
        print("Player one wins.")
    else:
        print("Still working on it") 

    print("Do you want to quit?\nType 'q' to quit\nTo play again, press any other key")

    user_quit = input()
    if user_quit.lower() == "q":
        break
    else:
        continue
    

