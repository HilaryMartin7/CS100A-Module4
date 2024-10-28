import random
import emoji
#set number of dice to 5 standard for yahtzee, could be modified with input later
total_dice = 5
#set number of turns to 3
turns = 3
       

def rollDice(n):
  """
  To roll dice initially based on total dice in game
  """
  rolls = [random.randint(1,6) for i in range (n)]
  return rolls


def chooseDiceReroll():
  """
  Prompts user to select dice to remove and roll again
  """
  while True:
    dice_to_remove = (input("Which dice would you like to roll again? or 'roll' when done removing: "))
    if dice_to_remove.lower() == 'roll':
      break
    dice_to_remove = int(dice_to_remove)
    currRolls.remove(dice_to_remove)
    print(f'Your current dice:  {currRolls}')


def rollDiceAgain(total_dice, currRolls):
  """
  If the number of dice in current roll is less than total, roll again using random
  Loop to do this for number of dice required to get to total of game (5)
  
  """
  dice_to_roll = total_dice - len(currRolls)
  print (f'\nRolling {dice_to_roll} dice.')
  for i in range (dice_to_roll):
    currRolls.insert((len(currRolls)), random.randint(1,6) )
 


currRolls = rollDice(total_dice)
print(f'Your current dice: {currRolls}')

while turns > 0:
  chooseDiceReroll()
  rollDiceAgain(total_dice, currRolls)
  turns-=1
  print (f'Your current dice:  {currRolls}')
print (emoji.emojize("Your game is over! Score your roll! :game_die:\n"))

