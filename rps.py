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
round_totals = int(input("How many rounds would you like to run? (There are 510 games in a round)"))
import random
for round in range(round_totals):
    print()
    for rps in range(10):
        rng = random.randint(1, 10)
        rps = random.randint(1,3)
        # 1 is rock, 2 is paper and 3 is scissors
        opponent.append(rng)
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
 #now we think based on previous decisions   

    for rps in range(500):
        rng = random.randint(1, 100)
        rps = opponent[random.randint(0, len(opponent) - 1)]
        if rng < 37:
            rng = 1
        else:
            if rng > 64:
                rng = 2
            else:
                rng = 3
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
print("RNG chose rock " + str(opponent.count(1) / len(opponent) * 100) + "% " "of the time")
print("RNG chose paper " + str(opponent.count(2) / len(opponent) * 100) + "% " "of the time")
print("RNG chose scissors " + str(opponent.count(3) / len(opponent) * 100) + "% " "of the time")