import random
total_dice = 5
num_kept_dice = 0
turns = 3

def rollDice(n):
  rolls = [random.randint(1,6) for i in range (n)]
  return rolls

currRolls = rollDice(total_dice)
print(currRolls)


while turns > 0:

    kept_dice = []
    while True:
        dice_to_keep = (input("Which dice would you like to keep? or 'none': "))
        if dice_to_keep.lower() == 'none':
            break
        kept_dice.append(dice_to_keep)
        print(kept_dice)

# nextRolls = rollDice(total_dice-len(kept_dice))
# print(nextRolls)

# while True:
#     reroll = input(f"first dice to re-roll (or none): ")
#     if reroll.lower()== "none":
#         break
#     currRolls.remove(reroll)


# dice = ['1','2','3','4','5','6']

# #Number of turns player has
# turns = 3

# #This is the group of dice kept by the player
# kept_dice = []

# def roll():
#     #This is the group of dice randomly chosen
#     rolled_dice = []

#     #Generate up to 5 random dice based on how many have been kept so far
#     for _ in range(5 - len(kept_dice)):

#         #Append random dice value to rolled_dice array
#         rolled_dice.append(random.choice(dice))

#     #Print roll group
#     print(rolled_dice)

#     dice_to_keep = int(input("Which dice would you like to keep? 1 - 5: "))
    
#     kept_dice.append(rolled_dice[dice_to_keep-1])



# while turns != 0:

#     #Let the user know how many turns they have left
#     print(f'You have {turns} turns left.')

#     #Roll dice
#     roll()

#     #Subtract 1 turn
#     turns -= 1

# #After all turns, show the kept dice:
# print("Kept dice:")
# print(kept_dice)
