import random

def get_user_choice():
    """Prompt the user for a valid choice: rock, paper, or scissors."""
    while True:
        user_input = input("\nEnter your choice (rock/paper/scissors): ").strip().lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")

def determine_winner(user, computer):
    """Return 'win', 'lose', or 'tie' based on the two choices."""
    if user == computer:
        return "tie"
    if (user == "rock" and computer == "scissors") or \
       (user == "scissors" and computer == "paper") or \
       (user == "paper" and computer == "rock"):
        return "win"
    return "lose"

def display_result(user_choice, computer_choice, result, user_score, computer_score):
    """Show the choices, the result, and the current score."""
    print("\n" + "=" * 40)
    print(f"  You chose: {user_choice.capitalize()}")
    print(f"  Computer chose: {computer_choice.capitalize()}")
    print("-" * 40)
    if result == "win":
        print("  🎉 You win this round! 🎉")
    elif result == "lose":
        print("  😞 You lose this round. 😞")
    else:
        print("  🤝 It's a tie! 🤝")
    print("-" * 40)
    print(f"  Score -> You: {user_score}  |  Computer: {computer_score}")
    print("=" * 40)

def play_again():
    """Ask the user if they want another round. Return True for yes, False for no."""
    while True:
        answer = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please answer 'yes' or 'no'.")

def main():
    """Main game loop."""
    print("\n✨ Welcome to Rock-Paper-Scissors! ✨")
    print("Instructions: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.\n")

    user_score = 0
    computer_score = 0
    playing = True

    while playing:
        user_choice = get_user_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = determine_winner(user_choice, computer_choice)

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        display_result(user_choice, computer_choice, result, user_score, computer_score)

        playing = play_again()

    print("\n🏁 Game over! Final score:")
    print(f"   You: {user_score}  |  Computer: {computer_score}")
    print("Thanks for playing! 👋")

if __name__ == "__main__":
    main()
