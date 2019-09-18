# Dice roller for The Spire
import random
cont = ''

def dice_check(): # Gets the number of dice to be rolled and ensures it's an integer
     while True:
        try:
            dice_roll = int(input('How many dice should be rolled? '))
        except ValueError:
            print("This is not an integer! Try again: ")
            continue
        else:
            return dice_roll
            break


def dice_range(): # Uses dice_check and then limits the number of dice to 1-4
    dice_num = dice_check()
    while dice_num > 4 or dice_num == 0:
        print('Number of dice must be between 1 and 4')
        dice_num = dice_check()
    return dice_num

def success_calculator(): # Calculates the result of the rolls as per The Spire
    success_pool = []
    dice = dice_range()
    while dice > 0:
        dice_roll=(random.randint(1, 10))
        success_pool.append(dice_roll)
        dice = dice-1
        high = max(success_pool)
    print (success_pool)
    if max(success_pool) == 10:
        print('Critical Success ' + str(high))
    elif max(success_pool) > 7:
        print('Success ' + str(high))
    elif max(success_pool) > 5:
        print('Success at a cost ' + str(high))
    elif max(success_pool) > 1:
        print('Failure ' + str(high))
    else:
        print('Critical failure ' + str(high))

#Main program
print ('Spire Dice Roller')
while cont != ('x' or 'X'):
    success_calculator()
    # cont = input('Input X to stop, anything else to roll again. ')
