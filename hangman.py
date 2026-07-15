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
    word = rand_word()
    print("\nWord to guess:\n")
    guessing = True
    prev_guesses = []
    display = len(word) * ["_"]
    dis = " ".join(display)
    print(dis)
    while lives > 0 and guessing:
        count = 0
        guess = input(
            f"\n\nPlease enter the letter or word you want to guess. ").lower()
        if not guess.isalpha():
            print("Only choose letters.")
        elif guess in prev_guesses:
            print("You have already guessed this!")
        elif len(guess) != 1 and guess != word:
            print("\nWrong word!")
            lives -= 1
            prev_guesses.append(guess)
            print(f"You now have {lives} lives remaining!")
        elif len(guess) != 1 and guess == word:
            print(f"Correct, the word was {word}!")
            guessing = False
        else:
            prev_guesses.append(guess)
            for index, character in enumerate(word):
                if character == guess:
                    count += 1
                    display[index] = character
                    print(" ".join(display))
                    if "".join(display) == word:
                        print(f"Correct, the word was {word}!")
                        guessing = False

            if count == 0:
                print("\nWrong character!")
                prev_guesses.append(guess)
                lives -= 1
                print(f"You now have {lives} lives remaining!")


hangman()
