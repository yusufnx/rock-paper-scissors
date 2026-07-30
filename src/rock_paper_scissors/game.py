import random

from InquirerPy import inquirer

POSSIBLE_CHOICES = ("Rock", "Paper", "Scissors")


def get_computer_choice() -> str:
    random_choice = random.choice(POSSIBLE_CHOICES)
    return random_choice


def get_user_choice() -> str:
    choice = inquirer.select(
        message="Select!", choices=POSSIBLE_CHOICES, vi_mode=True
    ).execute()

    return choice


def determine_winner(user_choice: str, computer_choice: str) -> str:
    beats = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper",
    }

    if user_choice == computer_choice:
        result = f"The game is a draw. Player picked: {user_choice}, Computer picked: {computer_choice}."
    elif beats[user_choice] == computer_choice:
        result = f"You won! Player picked: {user_choice}, Computer picked: {computer_choice}."
    else:
        result = f"You lost! Player picked: {user_choice}, Computer picked: {computer_choice}."

    return result


def play_game() -> None:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)

    print(result)


def main() -> None:
    print("Welcome to my game!")
    play_game()


if __name__ == "__main__":
    main()
