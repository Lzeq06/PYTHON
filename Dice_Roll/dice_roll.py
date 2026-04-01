# Ask User = Roll the dice? (Y,y/N,n) - Use all in lower, so then the only possible answers are y or n
# If Y,y - Roll the dice and print the number
# If N,n - Print "Goodbye" + message of "Thanks for playing" + Exit the program
# If any other answer - Print "Invalid input, please enter Y or N"

import random

while True:
    player_choice = input('Roll the dice? (Y,y/N,n): ').lower() 
    if player_choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1}, {dice2})')

    elif(player_choice == 'n'):
        print('Thanks for playing the game! Goodbye!')
        break

    else: 
        print('Invalid input, please enter Y or N')    
