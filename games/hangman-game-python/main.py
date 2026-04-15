import time
import random
from hangman_words import *
from hangman_art import *

print(logo)

word_to_guess = random.choice(word_list)
lives = 6
placeholder = "_" * len(word_to_guess)

correct_letters = []
letters_guessed = []
game_over = False

print(stages[lives])

while not game_over:

    print(f"Word to guess: {placeholder}")
    print(f"You have guessed: {letters_guessed}")
    user_letter_guess = input("Guess a letter: ").lower()

    if user_letter_guess in letters_guessed:
        print("Already guessed that, try again")
        time.sleep(1)
        print("\n" * 5)
        continue

    letters_guessed.append(user_letter_guess)

    if user_letter_guess in word_to_guess:
        correct_letters.append(user_letter_guess)
        print("Well Done, you guessed correct!")
    else:
        lives -= 1
        print(f"Incorrect, {user_letter_guess} is not in the word")
        print(stages[lives])

    time.sleep(1)
    print(f"*** {lives}/6 lives left ***")
    time.sleep(1)

    placeholder = ""
    for letter in word_to_guess:
        if letter in correct_letters:
            placeholder += letter
        else:
            placeholder += "_"

    print("\n" * 5)

    if "_" not in placeholder:
        print("🎉 YOU WIN! 🎉")
        print(f"the word was: {word_to_guess}")
        print(f"lives remaining: {lives}")
        game_over = True

    if lives == 0:
        print("You have run out of Lives, YOU LOSE!")
        print(f"The word was: {word_to_guess}")
        game_over = True
