# rock = 0
# paper = 1
# scissors = 2
# paper beats rock
# scissors beats paper
# rock beats scissors

print("Player 1: Type 0 for rock, type 1 for paper, type 2 for scissors")
first_player = int(input())
print("Player 2: Type 0 for rock, type 1 for paper, type 2 for scissors")
second_player = int(input())

if first_player == 1 and second_player == 0:
    print("Player 1 wins")
elif first_player == 2 and second_player == 1:
    print("Player 1 wins")
elif first_player == 0 and second_player == 2:
    print("Player 1 wins")
elif second_player == 1 and first_player == 0:
    print("Player 2 wins")
elif second_player == 2 and first_player == 1:
    print("Player 2 wins")
elif second_player == 0 and first_player == 2:
    print("Player 2 wins")
else:
    print("Still working on it")
