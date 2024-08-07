import random

# Function to get user's choice
def get_user_choice():
    while True:
        print("\nLet's play Rock, Paper, Scissors!")
        print("Enter your choice (rock, paper, scissors): ")
        user_choice = input().strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

# Function to get computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

# Function to display results
def display_results(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0
    play_again = True

    while play_again:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_results(user_choice, computer_choice, winner)

        # Update scores
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        # Display current scores
        print(f"\nYour score: {user_score} | Computer's score: {computer_score}")

        # Ask if the user wants to play again
        while True:
            play_again_input = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if play_again_input in ['yes', 'no']:
                break
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")

        if play_again_input == 'no':
            play_again = False

    print("\nThanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
