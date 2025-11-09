import random
import time

authPlayers = ["Jim","Tom","Jason","Nicky"]
bannedPlayers = ["Bob","Timothy","Jackson","Steve"]

score1 = 0
score2 = 0

# Player verification loop
while True:
    user1 = input("User 1, please enter your name (Case sensitive): ")

    if user1 in bannedPlayers:
        print("YOU ARE BANNED ❌")
        exit()
    elif user1 not in authPlayers:
        print("Ask Jim to apply.")
        exit()
    else:
        print("Verified ✅")

    user2 = input("User 2, please enter your name (Case sensitive): ")

    if user2 in bannedPlayers:
        print("YOU ARE BANNED ❌")
        exit()
    elif user2 not in authPlayers:
        print("Ask Jim to apply.")
        exit()
    elif user1 == user2:
        print("Can't be the same person. Restarting...")
        continue
    else:
        print("Verified ✅")
        break

# Countdown
for i in range(5, 0, -1):
    print(f"STARTING IN {i}s")
    time.sleep(1)
print()

# Dice rolling
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def calc_score(d1, d2):
    score = 0
    if d1 == d2:
        score += 10  # bonus for doubles
    if d1 % 2 == 0:
        score += d1 + 5
    else:
        score += d1
    if d2 % 2 == 0:
        score += d2 + 5
    else:
        score += d2
    return score

# Simulate rounds
for round_num in range(1, 6):
    print(f"🎲 ROUND {round_num} 🎲")
    dice1, dice2 = roll_dice()
    dice3, dice4 = roll_dice()

    print(f"{user1} rolled {dice1} and {dice2}")
    print(f"{user2} rolled {dice3} and {dice4}")

    score1 += calc_score(dice1, dice2)
    score2 += calc_score(dice3, dice4)

    print(f"Scores → {user1}: {score1} | {user2}: {score2}")
    print("-" * 30)
    time.sleep(1)

# Determine winner
print("🏁 FINAL RESULTS 🏁")
print(f"{user1}: {score1}")
print(f"{user2}: {score2}")

if score1 > score2:
    print(f"🎉 {user1} wins!")
elif score2 > score1:
    print(f"🎉 {user2} wins!")
else:
    print("It's a tie!")

for i in range(5, 0, -1):
    print(f"Closing IN {i}s")
    time.sleep(1)
print()
