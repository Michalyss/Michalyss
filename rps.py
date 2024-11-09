import time
import random


def rps(player_choice):
    outcomes = {
        "rock": ("scissors", "paper"),
        "paper": ("rock", "scissors"),
        "scissors": ("paper", "rock")
    }
    if player_choice not in ["rock", "paper", "scissors"]:
        print("\rInvalid choice. Choose rock, paper, or scissors.")
        return


    for x in range(0, 4):
        b = "The computer is thinking" + "." * x
        print(f"\r{b}", end="")
        time.sleep(1)

    if player_choice in outcomes:
        if random.randint(0, 1) == 0:
            print(f"\r{player_choice} beats {outcomes[player_choice][0]}. You win!")
        else:
            print(f"\r{outcomes[player_choice][1]} beats {player_choice}. You lose!")



