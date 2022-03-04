# Putting Together a Rock-Paper-Scissors Game in Python

<iframe width="560" height="315" src="https://www.youtube.com/embed/x99wfrb7tK0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The code when we get to the end of this video is the following:

```python
print("Enter 0 for Rock, Enter 1 for Paper, Enter 2 for Scissors")

print("Player 1, enter your number: ")
player_one = int(input())

print("Player 2, enter your number: ")
player_two = int(input())

for i in range(0, 3):
if player_one == player_two:
    print("Tie!")
elif player_one == 0 and player_two == 1:
    print("Player two wins.")
elif player_one == 0 and player_two == 2:
    print("Player one wins.")
else:
    print("Still working on it") 

```