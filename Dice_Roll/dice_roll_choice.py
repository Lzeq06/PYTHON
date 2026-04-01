# Ask User how many dices does he want to roll? (1,2,3,4,5,6) - Use all in lower, so then the only possible answers are 1,2,3,4,5 or 6
# Do a validation about the input, if the user enters a number that is not between 1 and 6, print "Invalid input, please enter a number between 1 and 6"
# If the user enters a valid number, continue the rolling process
# Ask User = Roll the dice? (Y,y/N,n) - Use all in lower, so then the only possible answers are y or n
# If Y,y - Roll the dice and print the number of dices that the user wants to roll
# If N,n - Print "Goodbye" + message of "Thanks for playing" + Exit the program
# If any other answer - Print "Invalid input, please enter Y or N"

import random
print("Welcome to the game, chosse the amount of dices you want to roll and then roll the dice as many times as you want! Let's start!")

while True:
    try:
        num_dices = int(input('How many dices do you want to roll? (1,2,3,4,5,6): '))
        if num_dices < 1 or num_dices > 6:
            print('Invalid input, please enter a number between 1 and 6')
        else:
            break

    except ValueError:
        print('Invalid input, please enter a number between 1 and 6')
        continue

while True:
    player_choice = input('Roll the dice? (Y,y/N,n): ').lower() 
    if player_choice == 'y':
        dice_rolls = [random.randint(1, 6) for _ in range(num_dices)]
        print(f'You rolled: {", ".join(map(str, dice_rolls))}')

    elif(player_choice == 'n'):
        print('Thanks for playing the game! Goodbye!')
        break

    else: 
        print('Invalid input, please enter Y or N')    
