import random
from hangman_words import word_list
from hangman_art import logo, stages
print(logo)

lives = 6



chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
incorrect_letters = []
while not game_over:


    print(f"**************************** {lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word and guess not in correct_letters:
        print(f"well done the letter {guess} is in the word")

    if guess in correct_letters or guess in incorrect_letters:
        print("you already guessed the letter: " + guess)
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1
        print("The letter " + guess + " in not in the word, you lose a life.")
        incorrect_letters.append(guess)
        if lives == 0:
            game_over = True


            print(f"***********************YOU LOSE**********************")
            print("the correct word is" + chosen_word)
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
