# Rock - Paper - Scissors
# Make a two-player Rock-Paper-Scissors game.
# Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

import random

# List of commands
commands = ["ROCK", "PAPER", "SCISSORS"]

# Prompts
cpu_wins = f"CPU Wins round!"
player_wins = f"Player wins this round!"
draw = f"It's a draw!"

# Random CPU command choice
cpu = commands[random.randint(0,2)]

# Set player to False
player = False

#Main game loop
while player == False:
    # Set player to True
    player = input("ROCK, PAPER or SCISSORS? ")
    if player == cpu:
        print(draw)
    elif player == "ROCK":
        if cpu == "PAPER":
            print(f" {cpu_wins} {cpu} covers {player}.")
        else:
            print(player_wins, f"{player} smashes {cpu}")
    elif player == "PAPER":
        if cpu == "SCISSORS":
            print(f"{cpu_wins} {cpu} cut {player}.")
        else:
            print(player_wins)
    elif player == "SCISSORS":
        if cpu == "ROCK":
            print(f"{cpu_wins} {cpu} smahses {player}.")
        else:
            print(f"{player_wins} {player} cut {cpu}.")
    else:
        print("No such command! Try again")
    player = False
    cpu = commands[random.randint(0,2)]