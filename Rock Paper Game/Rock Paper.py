import random

def game():
    choices = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(choices)

    while True:
        try:
            user_choice = input("Enter your choice (rock, paper, scissor) or 'q' to quit: ")
            if user_choice.lower() == 'q':
                return "Thanks for playing!"
            elif user_choice not in choices:
                print("Invalid input, please try again.")
                continue
            break
        except Exception as e:
            print("Invalid input, please try again.")

    print("Computer chose: ", computer_choice)

    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == 'rock' and computer_choice == 'scissor') or \
       (user_choice == 'scissor' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "Congratulations, you win!"
    else:
        return "Sorry, you lose. Better luck next time!"

while True:
    print(game())
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower()!= 'yes':
        break