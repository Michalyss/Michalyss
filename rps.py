import time
import random


def rps(player_choice):
    outcomes = {
        "rock": ("scissors", "paper"),
        "paper": ("rock", "scissors"),
        "scissors": ("paper", "rock")
    }
    for x in range(0, 4):
        b = "The computer is thinking" + "." * x
        print(f"\r{b}", end="")
        time.sleep(1)

    if player_choice in outcomes:
        if random.randint(0, 1) == 0:
            print(f"\r{player_choice} beats {outcomes[player_choice][0]}. You win!")
        else:
            print(f"\r{outcomes[player_choice][1]} beats {player_choice}. You lose!")
    else:
        print("\rInvalid choice. Choose rock, paper, or scissors.")