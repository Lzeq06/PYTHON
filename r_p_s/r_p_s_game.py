#Welcome User to the game
#User must choice between rock, paper, scissors 
#Ask User to enter his choice - Use all in lower, so then the only possible answers are r (rock), p(paper) or s (scissors)
#Generate a random choice for the computer - Use all in lower, so then the only possible
#answers are r (rock), p(paper) or s (scissors)
#Compare the user choice with the computer choice and print the result of the game

import random

print("Welcome to the Rock, Paper, Scissors Game!")

emojis = {'r': '✊', 'p': '✋', 's': '✌️'}
choices = ['r', 'p', 's']

while True:
    user_choice = input('Enter your choice (r, p, or s): ').lower()
    if user_choice not in choices:
        print('Invalid input, please enter r, p, or s.')
        continue

    computer_choice = random.choice(choices)

    print(f'You chose: {emojis[user_choice]}')
    print(f'Computer chose: {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print("It's a tie!")

    elif ((user_choice == 'r' and computer_choice == 's') or 
    (user_choice == 'p' and computer_choice == 'r') or 
    (user_choice == 's' and computer_choice == 'p')):
        print('Congratulations! You win!')

    else:
        print('Sorry, you lose. Better luck next time!')

    play_again = input('Do you want to play again? (Y,y/N,n): ').lower()

    if play_again == 'n':
        print('Thanks for playing the game! Goodbye!')
        break

    elif play_again != 'y':
        print('Invalid input, please enter Y or N')

