# -*- coding: utf-8 -*-
import random

def hangman():
    # 5 predefined words
    word_list = ['head', 'tail', 'coin', 'game', 'code']
    word = random.choice(word_list)
    guessed = ['_'] * len(word)
    tries = 6
    guessed_letters = []

    print("Welcome to Hangman! The word has", len(word), "letters.")
    print("Word:", ' '.join(guessed))

    while tries > 0 and '_' in guessed:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct✅!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            tries -= 1
            print("Wrong❌! You have {} tries left.".format(tries))

        print("Word:", ' '.join(guessed))

    if '_' not in guessed:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
