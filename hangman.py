from random import choice


def rand_word():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
        random_word = choice(words)
        return random_word


def hangman():
    lives = 7
    print("\nWelcome to Hangman!")
    print(
        f"\nYou have {lives} lives remaining, either guess the word letter by letter, or guess it all at once!")
    print(
        f"Keep your hangman off the contraption! \n{hangman_drawings[lives]}")
    word = rand_word()
    print("\nWord to guess:\n")
    guessing = True
    prev_guesses = []
    display = len(word) * ["_"]
    dis = " ".join(display)
    print(dis)
    while lives > 0 and guessing:
        count = 0
        if prev_guesses:
            print(f"\nPrevious guesses: {', '.join(prev_guesses)}")
        guess = input(
            f"\n\nPlease enter the letter or word you want to guess. \n\n").lower()
        if not guess.isalpha():
            print("Only choose letters.")
        elif guess in prev_guesses:
            print("You have already guessed this!")
        elif len(guess) != 1 and guess != word:
            print("\nWrong word!")
            lives -= 1
            if lives == 0:
                print(f"Bad luck! The word was {word}")
            prev_guesses.append(guess)
            print(f"You now have {lives} lives remaining!")
            print(hangman_drawings[lives])
        elif len(guess) != 1 and guess == word:
            print(
                f"Correct, the word was {word}!\nCongratulations, you win with {lives} lives remaining!")
            print(hangman_drawings[lives])
            guessing = False
        else:
            prev_guesses.append(guess)
            for index, character in enumerate(word):
                if character == guess:
                    count += 1
                    display[index] = character
                    if "".join(display) == word:
                        print(
                            f"Correct, the word was {word}!\nCongratulations, you win with {lives} lives remaining!")
                        print(hangman_drawings[lives])
                        guessing = False
                        break
            if count > 0 and guessing == True:
                print(f"\nGood guess, {guess} is in the word.")
                print(" ".join(display))
                print(hangman_drawings[lives])

            if count == 0:
                print("\nWrong character!")
                print(" ".join(display))
                lives -= 1
                if lives == 0:
                    print(f"Bad luck! The word was {word}")
                print(f"You now have {lives} lives remaining!")
                print(hangman_drawings[lives])


hangman_drawings = [r"""
  +---+         
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
                    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
                    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
                    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
                    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
                    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
                    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
                    r"""
  +---+
      |
      |
      |
      |
      |
========="""
                    ]


def play_again():
    while True:
        play = input(
            "Would you like to play again? Type 'y' for yes or 'n' for no: "
        ).lower()

        if play == "y":
            return True
        elif play == "n":
            return False
        else:
            print("Please type 'y' or 'n'.")


while True:
    hangman()
    if not play_again():
        print(f"\nThank you for playing!")
        break
