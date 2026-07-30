import pytest

from rock_paper_scissors.game import determine_winner


@pytest.mark.parametrize(
    ("user_choice", "computer_choice", "expected"),
    [
        ("Rock", "Rock", "draw"),
        ("Rock", "Paper", "lost"),
        ("Rock", "Scissors", "won"),
        ("Paper", "Rock", "won"),
        ("Paper", "Paper", "draw"),
        ("Paper", "Scissors", "lost"),
        ("Scissors", "Rock", "lost"),
        ("Scissors", "Paper", "won"),
        ("Scissors", "Scissors", "draw"),
    ],
)
def test_determine_winner(user_choice, computer_choice, expected):
    result = determine_winner(user_choice, computer_choice)

    assert expected in result.lower()
