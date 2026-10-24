import random

WORDS_WITH_HINTS = {
    "programming": [
        "python",
        "javascript",
        "compiler",
        "variable",
        "database",
        "algorithm",
    ],
    "animals": ["elephant", "kangaroo", "dolphin", "penguin", "cheetah", "octopus"],
    "countries": ["brazil", "australia", "canada", "germany", "japan", "egypt"],
    "movies": ["inception", "gladiator", "interstellar", "avatar", "matrix"],
}

HANGMAN_PICS = [
    """
   +---+
       |
       |
       |
      ===""",
    """
   +---+
   O   |
       |
       |
      ===""",
    """
   +---+
   O   |

   |   |
       |
      ===""",
    """
   +---+
   O   |
  /|   |
       |
      ===""",
    """
   +---+
   O   |
  /|\\  |
       |
      ===""",
    """
   +---+
   O   |
  /|\\  |
  /    |
      ===""",
    """
   +---+
   O   |
  /|\\  |
  / \\  |
      ===""",
]


def get_random_word(word_dict):
    category = random.choice(list(word_dict.keys()))
    word = random.choice(word_dict[category])
    return category, word


def display_game_state(hangman_pics, missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print("\nMissed letters:", " ".join(missed_letters) if missed_letters else "None")

    blanks = [
        letter if letter in correct_letters else "_" for letter in secret_word
    ]
    print("Word:", " ".join(blanks))
    print()


def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        else:
            return guess


def play_hangman():
    print("=========================================")
    print("           WELCOME TO HANGMAN            ")
    print("=========================================")

    category, secret_word = get_random_word(WORDS_WITH_HINTS)
    missed_letters = []
    correct_letters = []
    game_is_done = False

    print(f"Hint! The category is: **{category.upper()}**")

    while not game_is_done:
        display_game_state(
            HANGMAN_PICS, missed_letters, correct_letters, secret_word
        )

        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters.append(guess)

            found_all_letters = True
            for letter in secret_word:
                if letter not in correct_letters:
                    found_all_letters = False
                    break

            if found_all_letters:
                display_game_state(
                    HANGMAN_PICS, missed_letters, correct_letters, secret_word
                )
                print(
                    f"Yes! The secret word was '{secret_word}'! You have won!"
                )
                game_is_done = True
        else:
            missed_letters.append(guess)

            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_game_state(
                    HANGMAN_PICS, missed_letters, correct_letters, secret_word
                )
                print(
                    f"You have run out of guesses!\nAfter {len(missed_letters)} missed guesses and {len(correct_letters)} correct guesses, the word was '{secret_word}'"
                )
                game_is_done = True


if __name__ == "__main__":
    play_hangman()
