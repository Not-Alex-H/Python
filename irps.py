# rock paper scissors ai
# rps is the computer, rng is the random outcome
rps = 0
rng = 0
outcomes = []
winrate = 0
winrates = []
opponent = []
round = 1
total_outcomes = []
round_totals = 0
import random
import time
import os
os.system('cls')
def tie():
    print("Tie")

def lose():
    print("You lost")

def winner():
    print("You won!")

print()
time.sleep(1)
print("Welcome to Alex's machine learning Rock, Paper, Scissors game.")
time.sleep(2)
print("This game calculates how many times the computer would win against you based on a sample size of your choice")
time.sleep(2)
round_totals = int(input("How many sample games would you like to play?"))
time.sleep(2)
print("Please play Rock, Paper, Scissors as you normally would")
time.sleep(2)
for round_totals in range(round_totals):
    rng = input("rock, paper, scissors...")
    rps = random.randint(1,3)
    # 1 is rock, 2 is paper and 3 is scissors
    if rng == "rock":
        rng = 1
    else:
        if rng == "paper":
            rng = 2
        else:
            rng = 3
    opponent.append(rng)
    if rng == 1:
        if rps == 1:
            outcomes.append(0)
            tie()
        else:
            if rps == 2:
                outcomes.append(1)
                winner()
            else:
                outcomes.append(-1)
                lose()
    if rng == 2:
        if rps == 1:
            outcomes.append(-1)
            lose()
        else:
            if rps == 2:
                outcomes.append(0)
                tie()
            else:
                outcomes.append(1)
                winner()
    if rng == 3:
        if rps == 1:
            outcomes.append(1)
            winner()
        else:
            if rps == 2:
                outcomes.append(-1)
                lose()
            else: 
                outcomes.append(0)
                tie()
            
    win = outcomes[len(outcomes) - 1] 
#now we think based on previous decisions   
time.sleep(2)
print("The computer will now base its choices on your actions")
time.sleep(2)
round_totals = int(input("How many rounds would you like to simulate? (500 games in each round)"))
for round_totals in range(round_totals):  
    for rps in range(500):
        rng = opponent[random.randint(0, len(opponent) - 1)]
        rps = opponent[random.randint(0, len(opponent) - 1)]
        if rps == 1:
            rps = 3
        if rps == 2:
            rps = 1
        if rps == 3:
            rps = 2
        # 1 is rock, 2 is paper and 3 is scissors
        if rng == 1:
            if rps == 1:
                outcomes.append(0)
            else:
                if rps == 2:
                    outcomes.append(1)
                else:
                    outcomes.append(-1)
        if rng == 2:
            if rps == 1:
                outcomes.append(-1)
            else:
                if rps == 2:
                    outcomes.append(0)
                else:
                    outcomes.append(1)
        if rng == 3:
            if rps == 1:
                outcomes.append(1)
            else:
                if rps == 2:
                    outcomes.append(-1)
                else: outcomes.append(0)
        win = outcomes[len(outcomes) - 1] 

    print("round " + str(round))
    print("------------------------------------------------")
    print("There were " + str(outcomes.count(0)) + " draws")
    print("There were " + str(outcomes.count(-1)) + " losses")
    print("There were " + str(outcomes.count(1)) + " wins")
    print("The computer had a winrate of " + str(outcomes.count(1) / len(outcomes) * 100) + "%")
    round = round + 1
    total_outcomes.extend(outcomes)
    outcomes.clear()
print()
print("final")
print("------------------------------------------------")
print("There were " + str(total_outcomes.count(0)) + " draws")
print("There were " + str(total_outcomes.count(-1)) + " losses")
print("There were " + str(total_outcomes.count(1)) + " wins")
print("The computer had a final winrate of " + str(total_outcomes.count(1) / len(total_outcomes) * 100) + "%")
print("It lost " + str(total_outcomes.count(-1) / len(total_outcomes) * 100) + "%" + " of the games and drew " + str(total_outcomes.count(0) / len(total_outcomes) * 100) + "%" + " of the games")
print("RNG chose rock " + str(opponent.count(1) / len(opponent) * 100) + "% " "of the time")
print("RNG chose paper " + str(opponent.count(2) / len(opponent) * 100) + "% " "of the time")
print("RNG chose scissors " + str(opponent.count(3) / len(opponent) * 100) + "% " "of the time")